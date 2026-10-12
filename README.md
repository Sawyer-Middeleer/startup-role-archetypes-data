# Startup Role Archetypes — data

What recent Y Combinator startups are hiring people to do, organized into tasks and four overlapping activities: building, designing, selling, and operating.

[Explore Startup Role Archetypes](https://startup-role-archetypes.vercel.app)

The dataset covers job descriptions collected in October 2026 from eight YC cohorts, Fall 2024 through Summer 2026:

- 1,978 job descriptions across 499 companies
- 1,870 descriptions with explicitly stated tasks
- 104 task families and 1,243 normalized tasks, with 1,226 represented in these descriptions
- 16,040 distinct job–task assignments

Original job labels reflect titles and role context. Task activity labels describe the work extracted from each description, allowing a job to combine building, designing, selling, and operating.

## Files

Each table is available as JSON and CSV. CSV list fields contain JSON arrays.

- `jobs`: titles, source URLs, original activity labels, and task counts.
- `companies`: company identifiers, names, YC batches, and domains.
- `tasks`, `families`: normalized task and family definitions.
- `task_activities`: each task's activity labels.
- `job_tasks`: distinct job–task assignments.

See [SCHEMA.md](SCHEMA.md) for field definitions, [METHODOLOGY.md](METHODOLOGY.md) for collection and classification methods, and [manifest.json](manifest.json) for file counts and hashes.
