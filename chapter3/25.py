import json
import regex


with open("jawiki-uk.json") as f:
    uk = json.loads(f.readline())

dic = {}

text = uk["text"]
basic_information = [m for m in regex.findall(
    r'(?<rec>\{\{(?:[^\{\}]+|(?&rec))*\}\})', text) if "基礎情報" in m][0]
for elem in basic_information.split("\n|")[1:-1]:
    key, value = elem.replace("\n", "").split(" =")
    dic[key.strip()] = value.strip()

for key, value in dic.items():
    print(f"{key:<8}\t: {value}")
