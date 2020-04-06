N = int(input())
divisions = []

with open("popular-names.txt") as f:
    texts = f.readlines()
    lines = len(texts)
    divisions = [(lines + i) // N for i in range(N)]

offset = 0

for i, division in enumerate(divisions):
    with open(f"popular-names{i:02}.txt", "w") as f:
        f.write("".join(texts[offset: offset+division]))
    offset += divisions[i]
