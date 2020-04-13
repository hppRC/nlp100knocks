from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

train_df = pd.read_table("train.feature.txt", names=("title", "category"))
valid_df = pd.read_table("valid.feature.txt", names=("title", "category"))
test_df = pd.read_table("test.feature.txt", names=("title", "category"))

train_X, train_Y = train_df[["title"]], train_df[["category"]]
test_X, test_Y = test_df[["title"]], test_df[["category"]]

tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)

param_grid = [
            {'vect__ngram_range': [(1, 1)],
                'vect__stop_words': [None],
                'vect__tokenizer': [nltk.word_tokenize],
                'clf__penalty': ['l2'],
                'clf__C': [1.0, 10.0, 100.0]},
            {'vect__ngram_range': [(1, 1)],
                'vect__stop_words': [None],
                'vect__tokenizer': [nltk.word_tokenize],
                'vect__use_idf': [False],
                'vect__norm': [None],
                'clf__penalty': ['l2'],
                'clf__C': [1.0, 10.0, 100.0]}
            ]

lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf', LogisticRegression(random_state=0))])
gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='accuracy',
                           cv=5, verbose=1, n_jobs=-1)

gs_lr_tfidf.fit(np.ravel(train_X), np.ravel(train_Y))

clf = gs_lr_tfidf.best_estimator_
print(gs_lr_tfidf.best_params_)
print(gs_lr_tfidf.best_score_)
print(clf.score(np.ravel(test_X), np.ravel(test_Y)))