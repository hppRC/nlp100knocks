from util import extract_from_neko

for sentence in extract_from_neko():
    for i, token in enumerate(sentence):
        surface, base, pos, pos1 = token.values()

        if not (surface == "の" and pos == "助詞" and pos1 == "連体化"):
            continue
        if (i == 0 or i == len(sentence) - 1):
            continue

        pre = sentence[i - 1]
        nex = sentence[i + 1]

        if not (pre["pos"] == "名詞" and nex["pos"] == "名詞"):
            continue

        print(f"{pre['surface']}の{nex['surface']}")
