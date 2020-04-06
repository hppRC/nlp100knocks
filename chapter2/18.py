with open("popular-names.txt") as f:
    print(*sorted(f.readlines(), key=lambda x: -
                  int(x.strip().split("\t")[2])))
