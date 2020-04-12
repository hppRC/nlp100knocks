import json
import re

with open("jawiki-uk.json") as f:
    uk = json.loads(f.readline())

text = uk["text"]
print(*re.findall(r'^\[\[Category:(.*)\]\]$', text, re.MULTILINE), sep="\n")
