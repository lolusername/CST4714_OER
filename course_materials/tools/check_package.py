"""Read-only structural checks for the OER publication; Python standard library only.

This does not execute lessons, access cloud accounts, or certify accessibility.
Original code: MIT License, copyright (c) 2026 Atilio Barreda. See LICENSE.md.
"""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET
from zipfile import ZipFile


MATERIALS = Path(__file__).resolve().parents[1]
ROOT = MATERIALS.parent
ERRORS: list[str] = []
COUNTS: dict[str, int] = {}
LINK = re.compile(r"\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
SLIDE = re.compile(r"ppt/slides/slide\d+\.xml$")
NOTE = re.compile(r"ppt/notesSlides/notesSlide\d+\.xml$")


def check(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def check_links(path: Path, text: str) -> None:
    for target in LINK.findall(text):
        target = unquote(target.strip("<>"))
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        resolved = (path.parent / parsed.path).resolve()
        check(resolved.is_relative_to(ROOT) and resolved.exists(),
              f"Missing/outside link in {path.relative_to(ROOT)}: {target}")
        COUNTS["local_links"] = COUNTS.get("local_links", 0) + 1
    for notebook in re.findall(
        r"https://colab\.research\.google\.com/github/[^\s)<>\"]+", text
    ):
        prefix = "https://colab.research.google.com/github/lolusername/CST4714_OER/blob/main/"
        check(notebook.startswith(prefix), f"Unexpected Colab repository: {notebook}")
        if notebook.startswith(prefix):
            check((ROOT / notebook.removeprefix(prefix)).is_file(), f"Missing Colab notebook: {notebook}")


def main() -> int:
    files = [p for p in ROOT.rglob("*") if p.is_file() and not any(
        part.startswith(".") for part in p.relative_to(ROOT).parts
    )]
    for path in files:
        check(not path.is_symlink(), f"Unexpected symlink: {path.relative_to(ROOT)}")
        if path.suffix == ".md":
            check_links(path, path.read_text())
        if path.suffix == ".py":
            ast.parse(path.read_text(), filename=str(path))
        if path.suffix == ".csv":
            with path.open(newline="") as stream:
                rows = list(csv.reader(stream))
            check(bool(rows) and len(rows[0]) == len(set(rows[0])), f"Invalid CSV header: {path}")
            check(all(len(row) == len(rows[0]) for row in rows[1:]), f"Ragged CSV: {path}")

    root_entries = {p.name for p in ROOT.iterdir() if p.name != ".git"}
    check(root_entries == {"README.md", "Operating_Cloud_Databases.pdf", "course_materials"},
          "The public repository root must contain only the README, textbook PDF, and course_materials")
    book = ROOT / "Operating_Cloud_Databases.pdf"
    check(book.is_file() and book.read_bytes().startswith(b"%PDF-"), "Missing or invalid textbook PDF")
    check(not any(p.suffix in {".docx", ".epub", ".html"} for p in files),
          "Alternative textbook formats must not be published")
    for directory in ("oer_fellowship", "external_resources", "archive", "share"):
        check(not (ROOT / directory).exists(), f"Excluded directory present: {directory}")
        check(not (MATERIALS / directory).exists(), f"Excluded directory present: course_materials/{directory}")

    weeks = sorted((MATERIALS / "weeks").glob("week_[0-9][0-9]"))
    check(len(weeks) == 15, f"Expected 15 weekly folders, found {len(weeks)}")
    lab_count = 0
    slide_count = 0
    for week in weeks:
        check((week / "README.md").is_file(), f"Missing weekly guide: {week.name}")
        decks = list(week.glob("*.pptx"))
        labs = list(week.glob("lab_*.md"))
        lab_count += len(labs)
        check(bool(labs), f"No lab in {week.name}")
        check(len(decks) == 1, f"Expected one original deck in {week.name}")
        for deck in decks:
            check(deck.with_suffix(".pdf").is_file(), f"Missing PDF handout: {deck.name}")
            check(deck.with_name(deck.stem + "_transcript.md").is_file(), f"Missing transcript: {deck.name}")
            with ZipFile(deck) as archive:
                check(archive.testzip() is None, f"Invalid PowerPoint archive: {deck.name}")
                slides = [name for name in archive.namelist() if SLIDE.fullmatch(name)]
                notes = [name for name in archive.namelist() if NOTE.fullmatch(name)]
                slide_count += len(slides)
                check(len(slides) == len(notes), f"Slide/notes count mismatch: {deck.name}")
                for name in slides + notes:
                    ET.fromstring(archive.read(name))
    check(lab_count == 24, f"Expected 24 labs, found {lab_count}")
    check(slide_count == 321, f"Expected 321 slides, found {slide_count}")
    COUNTS.update(weeks=len(weeks), labs=lab_count, slides=slide_count)

    notebooks = sorted((MATERIALS / "notebooks").glob("*.ipynb"))
    check(len(notebooks) == 7, f"Expected seven notebooks, found {len(notebooks)}")
    for path in notebooks:
        notebook = json.loads(path.read_text())
        check(notebook.get("nbformat") == 4, f"Unexpected notebook format: {path.name}")
        for number, cell in enumerate(notebook["cells"], 1):
            source = cell["source"]
            text = source if isinstance(source, str) else "".join(source)
            if cell["cell_type"] == "markdown":
                check_links(path, text)
            if cell["cell_type"] == "code":
                check(not cell.get("outputs"), f"Saved output requires privacy review: {path.name}:{number}")
                check(cell.get("execution_count") is None, f"Saved execution count: {path.name}:{number}")
                lines = text.splitlines()
                if not any(line.lstrip().startswith(("!", "%")) for line in lines):
                    ast.parse(text, filename=f"{path.name}:cell{number}")
                COUNTS["code_cells"] = COUNTS.get("code_cells", 0) + 1

    data = json.loads((MATERIALS / "datasets/cisa_kev_sample/kev_sample.json").read_text())
    check(data["count"] == len(data["vulnerabilities"]) == 75, "CISA sample count must be 75")
    with (MATERIALS / "datasets/cisa_kev_sample/kev_sample.csv").open(newline="") as stream:
        csv_rows = list(csv.DictReader(stream))
    check([row["cveID"] for row in csv_rows] == [row["cveID"] for row in data["vulnerabilities"]],
          "CISA JSON and CSV record identifiers differ")
    check(len(list((MATERIALS / "assessments").glob("*.md"))) == 6, "Expected six assessment resources")
    for name in ("midterm_project.md", "final_project.md"):
        check((MATERIALS / "assignments" / name).is_file(), f"Missing project: {name}")
    COUNTS["notebooks"] = len(notebooks)
    print(json.dumps({"checks": COUNTS, "errors": ERRORS}, indent=2))
    if ERRORS:
        return 1
    print("PASS: structural checks only; no cloud, visual, or accessibility certification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
