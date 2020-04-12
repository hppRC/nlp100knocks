def extract_from_neko():
    result = []
    with open("./neko.txt.mecab") as f:
        sentence = []
        for line in f.readlines():
            if line.strip() == "EOS":
                if sentence:
                    result.append(sentence)
                sentence = []
            else:
                surface, rest = line.split("\t")
                if len(rest.split(",")) == 9:
                    pos, pos1, _, _, _, _, base, _, _ = rest.split(",")
                elif len(rest.split(",")) == 7:
                    pos, pos1, _, _, _, _, base = rest.split(",")

                tmp = {"surface": surface, "base": base,
                       "pos": pos, "pos1": pos1}
                sentence.append(tmp)
    return result
