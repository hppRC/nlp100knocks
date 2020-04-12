from utils import extract_from_neko

for sentence in extract_from_neko():
    for token in sentence:
        if token["pos"] == "動詞":
            print(token["base"])
