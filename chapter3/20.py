import json

with open("jawiki-country.json") as f:
    uk = [json.loads(line)["text"] for line in f.readlines()
          if json.loads(line)["title"] == "イギリス"]
    print(*uk)
