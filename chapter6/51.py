import nltk
from nltk import stem
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))


def create_features(data) -> list:
    title, category = data.strip().split("\t")
    title = title.replace("'", "")
    word_stem = stem.PorterStemmer().stem
    replaced = " ".join(
        map(
            lambda x: "stopword" if x in stopwords else word_stem(x),
            nltk.word_tokenize(title)
        )
    )
    return [title, replaced, category]


with open("train.txt") as f, open("train.feature.txt", "w") as f_f:
    features = [create_features(line) for line in f.readlines()]
    f_f.write("\n".join(["\t".join(feature) for feature in features]))
