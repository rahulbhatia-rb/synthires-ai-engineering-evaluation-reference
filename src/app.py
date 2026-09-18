import json, sys
from src.rubric import Evaluation, summarize
for line in sys.stdin:
    if line.strip():
        payload=json.loads(line)
        print(json.dumps({"input":payload,"result":summarize(Evaluation(**payload))}))
