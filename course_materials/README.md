# Course Materials

**PostgreSQL, MongoDB, and Reliable Data Systems**

Atilio Barreda | CST4714 Database Administration | Public teaching draft, September 2026

An open course about how database-backed applications work and how to keep their
data useful. It begins with a substantial relational-model and SQL review, then
develops practical skills in modeling, safe changes, transactions, permissions,
performance, recovery, document databases, and cloud operations.

## Start Here

- **[Download the complete textbook (PDF)](https://raw.githubusercontent.com/lolusername/CST4714_OER/main/Operating_Cloud_Databases.pdf)**: 190 pages, 15 chapters, equations, code listings, diagrams, and cloud-interface examples. The book is published in PDF form only.
- **[Weekly class materials](weeks/README.md)**: two meetings per week, slides, individual labs, readings, and notebook links.
- **[Run the notebooks](notebooks/README.md)**: nine core lessons and two supplementary SQL walkthroughs, with direct Open in Colab links.
- **[Instructor guides](instructor/README.md)**: lesson plans, demonstrations, troubleshooting, accessibility, and adaptation.
- **[Example syllabus (PDF)](CST4714_Fall_2026_Syllabus.pdf)** and [editable syllabus](syllabus.md): adapt the Fall 2026 dates, local policies, and submission arrangements before teaching another section.

No textbook purchase or paid database plan is required. Some linked platforms
require a free account; the weekly materials identify local or simulated
alternatives when cloud access is unavailable. Graded work is individual.

## Weekly Course Map

Each week has its own README. Start there for what to read, open, do, and submit.
Page numbers below refer to the textbook's printed page numbers. GitHub may not
jump to a PDF fragment; download the book and use its bookmarks or page field.

| Week | Focus and class materials | Textbook reading |
|---:|---|---|
| 1 | [Applications, DBMSs, and relational thinking](weeks/week_01/README.md) | [Chapter 1, p. 6](../Operating_Cloud_Databases.pdf#page=6), then the opening of [Chapter 2, p. 16](../Operating_Cloud_Databases.pdf#page=16) |
| 2 | [Major SQL review: filters, joins, grouping, and safe DML](weeks/week_02/README.md) | [Chapter 2, p. 16](../Operating_Cloud_Databases.pdf#page=16) |
| 3 | [Schemas, keys, constraints, and metadata](weeks/week_03/README.md) | [Chapter 3, p. 28](../Operating_Cloud_Databases.pdf#page=28) |
| 4 | [Views, identity columns, and safe schema changes](weeks/week_04/README.md) | [Chapter 4, p. 39](../Operating_Cloud_Databases.pdf#page=39) |
| 5 | [Transactions, MVCC, locks, and blocking](weeks/week_05/README.md) | [Chapter 5, p. 48](../Operating_Cloud_Databases.pdf#page=48) |
| 6 | [Roles, privileges, row-level security, and secrets](weeks/week_06/README.md) | [Chapter 6, p. 58](../Operating_Cloud_Databases.pdf#page=58) |
| 7 | [Query plans, selectivity, and index design](weeks/week_07/README.md) | [Chapter 7, p. 68](../Operating_Cloud_Databases.pdf#page=68) |
| 8 | [Backup, restore, and the midterm operations case](weeks/week_08/README.md) | [Chapter 8, p. 76](../Operating_Cloud_Databases.pdf#page=76) |
| 9 | [NoSQL history and models, JSON, and Atlas orientation](weeks/week_09/README.md) | [Chapter 9, p. 86](../Operating_Cloud_Databases.pdf#page=86) |
| 10 | [Basic MQL and document modeling](weeks/week_10/README.md) | [Chapter 10, p. 101](../Operating_Cloud_Databases.pdf#page=101) |
| 11 | [Aggregation, validation, indexes, and explain](weeks/week_11/README.md) | [Chapter 11, p. 116](../Operating_Cloud_Databases.pdf#page=116) |
| 12 | [Replication, consistency choices, and logical recovery](weeks/week_12/README.md) | [Chapter 12, p. 125](../Operating_Cloud_Databases.pdf#page=125) |
| 13 | [Capacity, shard keys, Python, and public-data imports](weeks/week_13/README.md) | [Chapter 13, p. 140](../Operating_Cloud_Databases.pdf#page=140) |
| 14 | [Polyglot systems, outbox pattern, and incident repair](weeks/week_14/README.md) | [Chapter 14, p. 153](../Operating_Cloud_Databases.pdf#page=153) |
| 15 | [Integrated review, portfolios, and interviews](weeks/week_15/README.md) | [Chapter 15, p. 165](../Operating_Cloud_Databases.pdf#page=165) |

## Companion Collection

The [OER catalog](OER_CATALOG.md) describes every resource and its educational
contribution: 15 weekly guides, 24 labs, 11 notebooks, three data packages,
15 original PowerPoints with 380 slides and speaker scripts, matching PDF handouts and text
transcripts, six assessment resources, two major projects, and five adoption
and release guides. The book's 15 chapters are the 15 text modules, not an
additional set of materials.

- [Midterm](assignments/midterm_project.md) and [final project](assignments/final_project.md).
- [Diagnostic, writing responses, retrieval practice, and rubrics](assessments/README.md).
- [Metro Support data](datasets/metro_support/README.md), [Mini Inventory data](datasets/mini_inventory/README.md), and [CISA KEV teaching sample](datasets/cisa_kev_sample/README.md).
- [Reusable diagrams](figures/README.md) and [course alignment map](course_map.md).

Download the entire collection with GitHub's **Code > Download ZIP**, or clone it:

```bash
git clone https://github.com/lolusername/CST4714_OER.git
```

## Reuse and Review

Edit the weekly guides, labs, assignments, and transcripts as Markdown; edit
slides in PowerPoint and notebooks in Colab or Jupyter. Textbook source files,
Word/HTML/EPUB book editions, vendor-owned presentations, private grading files,
and fellowship administration records are not part of this repository.

This is a **public teaching draft**, updated September 25, 2026, not a claim of
external peer review, institutional approval, or accessibility certification.
The full sequence has been revised, with local example tests and visual reviews.
Fresh hosted Colab/cloud end-to-end testing and full accessibility review are
not claimed. The catalog distinguishes these limits from completed content.
Rehearse the selected labs and check current platform limits before teaching.
Slide transcripts are included; PDF reading order still needs accessibility
review. Use the [adaptation guide](instructor/accessibility_adaptation.md) when
a student needs an equivalent format or activity.

Unless a file states otherwise, original instructional content is **CC BY-NC-SA
4.0**, original code is **MIT**, and the synthetic datasets are **CC0**. The
Week 12-15 transcripts retain their **CC BY 4.0** notices. The CISA sample retains its source's CC0
terms. Product-interface elements, trademarks, and attributed third-party
excerpts retain their owners' rights; they are not relicensed by this project.
External courses and documentation are linked references, not files claimed as
original OER. See [licenses](LICENSE.md), [attributions](ATTRIBUTIONS.md), and
[citation metadata](CITATION.cff).

Contact: [abarreda@citytech.cuny.edu](mailto:abarreda@citytech.cuny.edu).
