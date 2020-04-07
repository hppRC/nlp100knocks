import json

with open("jawiki-uk.json") as f:
    uk = [json.loads(line) for line in f.readlines()]
    print(*map(lambda x: ", ".join(x["category"]), uk))
