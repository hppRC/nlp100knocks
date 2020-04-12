import json
import re

with open("jawiki-uk.json") as f:
    uk = json.loads(f.readlines()[0])
text = uk["text"]
m = re.findall(r'^\[\[Category:.*\]\]$', text, re.MULTILINE)
print(*m, sep="\n")
