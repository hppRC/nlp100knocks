import json
import re

with open("jawiki-uk.json") as f:
    uk = json.loads(f.readline())

text = uk["text"]
for m in re.findall(r'^\s*(=+)\s*([^=]*)\s*=+', text, re.MULTILINE):
    print(f"level: {len(m[0])}, name: {m[1]}")
