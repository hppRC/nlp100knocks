import collections
from utils import extract_from_neko

words = []

for sentence in extract_from_neko():
    for elem in sentence:
        words.append(elem["surface"])

counts = collections.Counter(words).most_common()
for count in counts:
    word, num = count
    print(f"{word: <8}\t: {num}")
