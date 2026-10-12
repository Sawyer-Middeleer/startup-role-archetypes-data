# Schema, version 1

All identifiers are strings. Tables contain no source-description or quotation fields.

| Table | Fields |
|---|---|
| jobs | `job_id`: stable employer-description unit; `company_id`: YC ID; `title`; `source_url`; `original_activities`: equal overlapping labels; `has_task_evidence`: boolean; `task_count`: distinct supported canonical tasks |
| companies | `company_id`; `name`; `batch`; `domain`: public company website host, possibly empty |
| tasks | `task_id`; `family_id`; `name`; `definition` |
| families | `family_id`; `name`; `definition` |
| task_activities | `task_id`; `activities`: nonempty unique subset of building/designing/selling/operating |
| job_tasks | `job_id`; `task_id`; the pair is unique |

Only HTTP(S) source URLs are included. Email application links and unavailable URLs are represented as empty strings. All job and family references must resolve. The full taxonomy includes 17 tasks with no strict assignment in this snapshot. Do not drop those silently when reporting taxonomy size.

Compute a job's activity share by giving each distinct task one unit, divided equally across its mapped activities, then dividing activity totals by the job's task count. A job with zero tasks has an unknown composition, not four measured zeros. Do not use source observation counts as task weights.

For “Beyond the archetype,” select jobs whose `original_activities` includes the activity of interest. Count distinct selected jobs per task, then divide by all selected jobs, including those without extracted tasks. Activity groups overlap; their totals must not be added.
