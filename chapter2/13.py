with open("merged.txt", "w") as f, open("col1.txt") as f_col1, open("col2.txt") as f_col2:
    buffer = []
    for col1, col2 in zip(f_col1.readlines(), f_col2.readlines()):
        buffer.append(f"{col1.strip()}\t{col2.strip()}")
    f.write("\n".join(buffer))
