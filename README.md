# Startup Role Archetypes — data

A snapshot of the work recent Y Combinator startups advertised in October 2026, organized into tasks and four overlapping activities: building, designing, selling, and operating.

[Explore the interactive preview](https://startup-role-archetypes-7c1pfcxkx-sawyermiddeleers-projects.vercel.app) — Vercel authentication may be required during preview.

The release contains 1,978 eligible employer-description units across 499 companies. Of these, 1,870 have explicit, required task evidence; 108 have no supported task composition. There are 104 task families and 1,243 canonical tasks, of which 1,226 occur in this release's strict evidence subset. The 16,040 job-task pairs count each canonical task once per job. These are description units, not verified unique vacancies or hires.

## Files

Each table is available as JSON and CSV. CSV list fields contain JSON arrays. See [SCHEMA.md](SCHEMA.md), [METHODOLOGY.md](METHODOLOGY.md), and [manifest.json](manifest.json).

- `jobs`: source URLs, titles, original activity labels, evidence availability.
- `companies`: public company identifiers, names, batches, and domains.
- `tasks`, `families`: normalized definitions.
- `task_activities`: independent mapping of each task to one or more activities.
- `job_tasks`: deduplicated explicit, required task assignments.

Original job labels and task composition answer different questions. Original labels incorporate the role's identity and source context. Task composition measures the distribution of extracted, normalized responsibilities. Neither replaces the other.

## Scope and limitations

This is an observed posting snapshot, not a live job board. Missing task evidence does not mean a job does no work. Missing activity evidence does not establish that an activity is absent in practice. Detailed descriptions yield more extractable tasks; normalization granularity affects task shares. Shares do not measure time, importance, or employee behavior.

The source collection covered eight YC cohorts, Fall 2024 through Summer 2026. Its bounded crawl can miss postings. This export contains companies with retained jobs, not the entire roster. It cannot establish historical change, startup-versus-incumbent differences, or an AI causal effect.

Normalization remains provisional. Known examples include Harper's GTM Engineer, whose predictive-model assignment rests on broad model language, and Artificial Societies' Growth Engineer, where demo datasets may have been normalized too specifically as training data. Family clustering also obscures some commercial roles. These caveats apply to interpretations of the data, not only chart labels.

## Reuse and provenance

Public-source metadata and independently normalized annotations are provided here. Full job descriptions, verbatim evidence quotations, archived pages, model working files, People Data Labs enrichment, personal emails, phone numbers, street addresses, and personal profile links are excluded. Public company names, job titles, and source-posting links are retained. Source URLs allow readers to consult publishers; pages may have changed or disappeared.

No blanket license grant is asserted for third-party source material. This release does not claim ownership of employer titles or public metadata. A reusable-data license has not yet been assigned; consult the repository owner before redistribution under an assumed license.

Run `python3 validate.py` to check file hashes, referential integrity, task counts, and composition invariants. The checks reproduce the released table structure and calculations; without private source snapshots they cannot independently verify extraction judgments.
