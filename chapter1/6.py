def bi_gram(list_or_str):
    return [list_or_str[i: i + 2] for i in range(len(list_or_str) - 1)]


X = set(bi_gram("paraparaparadise"))
Y = set(bi_gram("paragraph"))
print(X | Y)  # union
print(X & Y)  # intersection
print(X - Y)  # difference
print("se" in X | Y)
