import json
import re


with open("jawiki-uk.json") as f:
    uk = [json.loads(line) for line in f.readlines()]
    for article in uk:
        text = article["text"]
        m = re.findall(r'\{\{基礎情報 国\n\|(.*)\n\|(.*)(?:(?:\n\|(.*))*)', text)
        print(m)
