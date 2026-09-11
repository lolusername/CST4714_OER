# CISA Known Exploited Vulnerabilities Teaching Sample

This package is a small, versioned subset of the U.S. Cybersecurity and
Infrastructure Security Agency's Known Exploited Vulnerabilities catalog. It is
used to practice data-source evaluation, JSON/CSV inspection, idempotent import,
aggregation, capacity reasoning, and candidate shard-key analysis.

## Files

- `kev_sample.json`: source metadata plus 75 selected vulnerability records.
- `kev_sample.csv`: the same selected fields in a flat format; CWE arrays use `|`
  as the within-cell separator.

## Transformation

[The dataset builder](../../tools/build_datasets.py) retrieves the official JSON feed, selects the first 75
records in source order, and keeps only:

- CVE ID;
- vendor/project;
- product;
- vulnerability name;
- date added;
- due date;
- known ransomware campaign use; and
- CWE list.

The snapshot metadata records the source catalog version, source release time,
retrieval time, URL, and selection. Descriptions, remediation text, and notes are
omitted to keep the classroom fixture compact. The sample is not a complete or
current vulnerability-management source.

## Source and Use

Official feed:
<https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json>

CISA distributes the KEV database under **CC0 1.0**, as stated in its
[official KEV repository license](https://github.com/cisagov/kev-data/blob/develop/LICENSE).
This teaching subset retains that CC0 status. The CISA logo, DHS seal, and
third-party material linked from source records are not covered by that data
dedication. CISA does not endorse this course.

Course-authored transformation code is MIT licensed; this README is CC BY-NC-SA
4.0. The preserved sample is a dated classroom fixture, not a live feed. Running
the builder replaces the sample with a newly dated snapshot, so recheck any lab
examples that depend on particular records before distributing an update.

## Safety

The catalog identifies publicly known vulnerabilities. It does not contain
exploit code and is not a substitute for current CISA guidance, asset inventory,
risk assessment, or professional vulnerability management.
