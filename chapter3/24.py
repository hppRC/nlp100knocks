import json
import re


with open("jawiki-uk.json") as f:
    uk = [json.loads(line) for line in f.readlines()]
    for article in uk:
        text = article["text"]
        media = re.findall(r'\[\[ファイル:(.*?)(\|.*)*\]\]', text)
        print(*map(lambda x: x[0], media), sep="\n")
