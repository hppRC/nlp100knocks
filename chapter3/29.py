import regex
import json
import requests

with open("jawiki-uk.json") as f:
    uk = json.loads(f.readline())

dic = {}

text = uk["text"]
basic_information = [m for m in regex.findall(
    r'(?<rec>\{\{(?:[^\{\}]+|(?&rec))*\}\})', text) if "基礎情報" in m][0]
for elem in basic_information.split("\n|")[1:-1]:
    key, value = elem.replace("\n", "").split(" =")
    dic[key.strip()] = value.strip()

url = "https://ja.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"File:{dic[u'国旗画像']}"
}

res = requests.get(url, params)
res_url = res.json()["query"]["normalized"][0]["to"]

print(f"https://ja.wikipedia.org/wiki/イギリス#/media/{res_url}")
