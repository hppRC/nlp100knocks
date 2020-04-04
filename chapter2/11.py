with open("popular-names.txt", "r") as f:
    for line in f.readlines():
        print(line.strip().replace("\t", " "))
