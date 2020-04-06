import collections

with open("popular-names.txt") as f:
    first_columns = [line.strip().split("\t")[0] for line in f.readlines()]
    [print(x[1], x[0]) for x in sorted(collections.Counter(
        first_columns).items(), key=lambda x: int(x[1]))]
