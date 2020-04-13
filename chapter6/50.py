import random
from collections import defaultdict

counter = defaultdict(int)

with open("newsCorpora.csv") as f:
    dataset = []
    for line in f.readlines():
        data = line.split("\t")
        # id, title, url, publisher, category, story, hostname, timestamp = row
        _, title, _, publisher, category, _, _, _ = data
        if publisher in ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]:
            dataset.append([title, category])
            counter[category] += 1


random.shuffle(dataset)

train = dataset[: int(len(dataset) * 0.8)]
valid = dataset[int(len(dataset) * 0.8): int(len(dataset) * 0.9)]
test = dataset[int(len(dataset) * 0.9):]


with open("train.txt", "w") as f:
    f.write("\n".join(["\t".join(data) for data in train]))

with open("valid.txt", "w") as f:
    f.write("\n".join(["\t".join(data) for data in valid]))

with open("test.txt", "w") as f:
    f.write("\n".join(["\t".join(data) for data in test]))

print(counter.items())
