import json

with open("jawiki-uk.json") as f:
    uk = [json.loads(line) for line in f.readlines()]
    print(*map(lambda x: "\n".join(x["category"]), uk))
