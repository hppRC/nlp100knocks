import json

with open("jawiki-country.json") as f:
    articles = [json.loads(line) for line in f.readlines()]
    uk = [article
          for article in articles if article["title"] == "イギリス"]
    print(*[article["text"] for article in uk])

with open("jawiki-uk.json", "w") as f:
    f.write("\n".join(map(lambda x: json.dumps(x, ensure_ascii=False), uk)))
