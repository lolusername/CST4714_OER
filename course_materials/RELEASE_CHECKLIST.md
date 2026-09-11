# Adaptation and Publication Checks

This is a reusable checklist for instructors adapting the collection, not a
certificate that every check has passed. The [catalog](OER_CATALOG.md) records
the current draft's scope and review limits.

## Preserve a Teachable Sequence

- [ ] Keep assigned readings, classroom examples, and the lab's starting data aligned.
- [ ] Rehearse each chosen activity from a new student account or clean local environment.
- [ ] Keep the substantial SQL review before work that assumes SQL fluency.
- [ ] State individual-work expectations and one clear submission for each lab.
- [ ] Keep the instructor's demonstration distinct from the student's practice.
- [ ] Keep project requirements in the canonical assignment, not duplicated across weekly pages.
- [ ] Check that the no-cost fallback teaches the intended concept and clearly states simulation limits.

## Check Files and Examples

Run the local, read-only package check from the repository root:

```bash
python3 course_materials/tools/check_package.py
```

It checks file structure, relative links, notebook syntax and saved-output
hygiene, paired presentation formats, and dataset structure. It does not log in
to cloud services, execute labs, certify pedagogy, or validate accessibility.

- [ ] Run notebook paths and SQL in disposable databases; test cleanup and reruns.
- [ ] Open Colab links and account-gated external activities in the actual teaching environment.
- [ ] Recheck vendor free-tier and network requirements using current official documentation.
- [ ] Read commands before running them; do not target a production database.
- [ ] Inspect every changed slide and exported PDF page for clipping, contrast, and notation.
- [ ] Keep speaker notes and text transcripts in the same slide order and wording.

## Accessibility and Rights

- [ ] Check keyboard navigation, reading order, mathematical notation, code selection, and diagram descriptions.
- [ ] Arrange equivalent formats or activities where the PDF or a cloud service creates an access barrier.
- [ ] Preserve licenses and attribution; identify changed material and third-party exceptions.
- [ ] Check data provenance and licensing; do not treat free access as reuse permission.
- [ ] Remove secrets, personal data, real connection strings, and private grading records, including notebook outputs.
- [ ] Record the tested environment, date, remaining limits, and changes in the adopting repository.

The textbook in this repository is deliberately PDF-only. The companion labs,
notebooks, slides, transcripts, datasets, and guides remain editable. Do not
accidentally add alternative book formats, private working files, or vendor-owned
presentations while publishing an adaptation.
