# Methodology

The public roster was seeded from the [unofficial yc-oss directory mirror](https://github.com/yc-oss/api) and checked against [Y Combinator company pages](https://www.ycombinator.com/companies). The collector followed company careers links and public Ashby, Greenhouse, and Lever job-board interfaces, plus structured job data and reviewed custom pages. Saved collection evidence remains private. Collection was bounded, not an exhaustive crawl of each domain.

Captured posting URLs were grouped into employer-description units using whitespace-identical descriptions within employers. General applications and explicitly closed postings were excluded from current-hiring prevalence. Source checks do not guarantee vacancies remained open.

Workers extracted duties with supporting source evidence before global families were named. All 1,981 initial units were reviewed in 45 chunks. Family normalization preceded concrete-task normalization. Saved adjudications corrected omissions and over-specific assignments. Independent reviews sampled original postings and mappings; they did not individually adjudicate every final task assignment. The final eligible count is 1,978.

This release retains only explicit, required duties. It deduplicates canonical tasks within each job. The taxonomy contains 104 families and 1,243 tasks. AI/human evidence, inferred duties, optional duties, and original quotations are outside the release.

The four activities are equal, overlapping labels. Building covers engineering and relevant technical research; designing covers creative and product design; selling covers demand creation and commercial work; operating covers delivery and organizational work. The task crosswalk was constructed independently of original job labels, using family defaults and task-specific exceptions. It remains provisional across individual occurrence contexts.

Each distinct task contributes one unit divided equally among its activities. Summed weights divided by task count produce task shares. These are shares of coded tasks, not time or importance. Repeated source evidence for one task does not increase its weight.

Original activity labels remain a separate source classification. They incorporate title and role context that task counts may underrepresent. Description emphasis and semantic normalization can create disagreements between original labels and task mix.

The manifest records an SHA-256 hash of the input explorer snapshot and each exported table. Table derivations can be reproduced from this release; reproducing extraction requires source snapshots and saved worker judgments not redistributed here. A fresh scrape or fresh model run will not reproduce the same snapshot or semantic decisions.
