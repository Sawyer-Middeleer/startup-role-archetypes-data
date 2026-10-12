#!/usr/bin/env python3
"""Validate the released data without private files or dependencies."""
import hashlib,json,re
from collections import Counter
from pathlib import Path
p=Path(__file__).resolve().parent
load=lambda n:json.loads((p/(n+'.json')).read_text())
m=load('manifest')
for name,digest in m['files'].items():
    assert hashlib.sha256((p/name).read_bytes()).hexdigest()==digest,name
schema={'jobs':{'job_id','company_id','title','source_url','original_activities','has_task_evidence','task_count'},'companies':{'company_id','name','batch','domain'},'tasks':{'task_id','family_id','name','definition'},'families':{'family_id','name','definition'},'task_activities':{'task_id','activities'},'job_tasks':{'job_id','task_id'}}
data={name:load(name) for name in schema}
for name,rows in data.items():
    assert all(set(r)==schema[name] for r in rows),name
jobs={r['job_id']:r for r in data['jobs']};tasks={r['task_id']:r for r in data['tasks']};families={r['family_id']:r for r in data['families']};companies={r['company_id']:r for r in data['companies']};activities={r['task_id']:r['activities'] for r in data['task_activities']}
for name,mapping in [('jobs',jobs),('tasks',tasks),('families',families),('companies',companies),('task_activities',activities)]:assert len(mapping)==len(data[name])
allowed={'building','designing','selling','operating'}
assert set(activities)==set(tasks)
assert all(a and len(a)==len(set(a)) and set(a)<=allowed for a in activities.values())
assert all(j['original_activities'] and set(j['original_activities'])<=allowed and j['company_id'] in companies for j in jobs.values())
assert all(t['family_id'] in families for t in tasks.values())
pairs={(r['job_id'],r['task_id']) for r in data['job_tasks']};assert len(pairs)==len(data['job_tasks'])
assert all(j in jobs and t in tasks for j,t in pairs)
counts=Counter(j for j,t in pairs)
assert all(j['task_count']==counts[uid] and j['has_task_evidence']==bool(counts[uid]) for uid,j in jobs.items())
for uid in jobs:
    weights=Counter()
    for j,t in pairs:
        if j==uid:
            for a in activities[t]:weights[a]+=1/len(activities[t])
    assert abs(sum(weights.values())-counts[uid])<1e-8
actual=dict(jobs=len(jobs),companies=len(companies),jobs_with_tasks=sum(bool(counts[j]) for j in jobs),tasks=len(tasks),represented_tasks=len({t for j,t in pairs}),families=len(families),job_task_pairs=len(pairs))
assert actual==m['counts']
print('PASS:',json.dumps(actual))

for name in m['files']:
    text=(p/name).read_text()
    assert not re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',text,re.I),name
    assert '/Users/' not in text and 'PRIVATE KEY' not in text,name
print('PASS: no email addresses, local home paths, or private-key markers in exported tables')
