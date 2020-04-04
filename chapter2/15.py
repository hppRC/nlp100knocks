import sys

with open("popular-names.txt") as f:
    for line in f.readlines()[-int(sys.argv[1]):]:
        print(line.strip())
