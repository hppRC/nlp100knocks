def n_gram(list_or_str, n):
    return [list_or_str[i: i + n] for i in range(len(list_or_str) - n + 1)]


print(n_gram("I am an NLPer".split(" "), 2))
print(n_gram("I am an NLPer", 2))
