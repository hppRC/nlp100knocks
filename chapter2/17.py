with open("popular-names.txt") as f:
    first_columns = set(line.strip().split("\t")[0] for line in f.readlines())
    print(*sorted(first_columns), sep="\n", end="")
