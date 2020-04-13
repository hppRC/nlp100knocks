import nltk
from nltk import stem
from nltk.corpus import stopwords
import re

stopwords = set(stopwords.words('english'))
mapper = {"b": "0", "t": "1", "e": "2", "m": "3"}
# word_stem = stem.PorterStemmer().stem

def create_features(data) -> list:
    features = []
    labels = []
    for title, category in map(lambda x: x.strip().split("\t"), data):
        replaced = " ".join(
            map(
                lambda x: "STOPWORD" if x in stopwords else x,
                nltk.word_tokenize(re.sub(r"['\"|!,.(){}*-]", "", title))
            )
        )
        features.append(replaced)
        labels.append(mapper[category])

    return ["\t".join(row) for row in zip(features, labels)]


for source, output in [["train.txt", "train.feature.txt"], ["valid.txt", "valid.feature.txt"], ["test.txt", "test.feature.txt"]]:
    with open(source) as f, open(output, "w") as f_f:
        features = create_features(f.readlines())
        f_f.write("\n".join(features))
