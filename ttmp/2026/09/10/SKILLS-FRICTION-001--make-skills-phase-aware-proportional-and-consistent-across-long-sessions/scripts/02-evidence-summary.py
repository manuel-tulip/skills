"""Summarize bounded, verified facts; do not treat profile heuristics as timing proof.
Usage: python3 02-evidence-summary.py SNAPSHOT_JSONL
"""
import collections,hashlib,json,pathlib,sys
sources=pathlib.Path(__file__).resolve().parents[1]/'sources'
native=pathlib.Path(sys.argv[1]); kinds=collections.Counter()
for line in native.open():
    event=json.loads(line)
    kinds[event.get('type')]+=1
profile=json.loads((sources/'doc-consumption.json').read_text())[0]['profiles']['01a0837a-fb1c-7183-9bf5-26fce6d60551']
reads=collections.Counter(item['file'] for item in profile['skill_file_reads'] if item['turn']<1505)
api=json.loads((sources/'api-calls.json').read_text())[0]
print(json.dumps({'snapshot_sha256':hashlib.sha256(native.read_bytes()).hexdigest(),
 'pre_postmortem_turn_cutoff':1505,'explicit_skill_reads_before_cutoff':dict(reads),
 'native_compaction_records':kinds['compaction'],
 'heuristic_cache_collapse_candidates':len(api['compaction_events']),
 'corrections':['Cache-collapse candidates are not native compaction events.',
 'Zero ticket-read/help profile counts contradict inspected calls; do not infer non-use.',
 'Read counts exclude pinned or implicit prompt inclusion.',
 'No causal elapsed-time or dollar-cost attribution is made.']},indent=2))
