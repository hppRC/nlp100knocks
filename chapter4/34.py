from utils import extract_from_neko

for sentence in extract_from_neko():
    tmp = ""
    word_count = 0
    for token in sentence:
        surface, _, pos, _ = token.values()
        if pos == "名詞":
            tmp += surface
            word_count += 1
        elif tmp and word_count >= 2:
            print(tmp)
            tmp = ""
            word_count = 0
        else:
            tmp = ""
            word_count = 0
