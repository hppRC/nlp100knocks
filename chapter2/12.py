names = []
genders = []

with open("popular-names.txt", "r") as f:
    for line in f.readlines():
        (name, gender, _, _) = line.strip().split("\t")
        names.append(name)
        genders.append(gender)

with open("col1.txt", "w") as f:
    f.write("\n".join(names))

with open("col2.txt", "w") as f:
    f.write("\n".join(genders))
