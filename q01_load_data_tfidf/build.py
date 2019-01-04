# %load q01_load_data_tfidf/build.py
# Default imports

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files
from nltk.tokenize import TreebankWordTokenizer

path = 'data/sessions.csv'
# Write your solution here :
def q01_load_data_tfidf(path,max_df=0.95,min_df=2,no_features=1000):
    dataset = pd.read_csv(path)
    tfidf_vectorizer = TfidfVectorizer(max_df=max_df, min_df=min_df, max_features=no_features, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(dataset['talkTitle'])
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    return dataset, tfidf, tfidf_feature_names


