import pickle
from crawler import load_data
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# http://scikit-learn.org/stable/modules/feature_extraction.html

def _build_vectorizer(X_train):
    corpus = [x['title'] for x in X_train]
    vectorizer = CountVectorizer(min_df=1)
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

def _test_to_vector(X_test, vectorizer):
    return vectorizer.transform([x['title'] for x in X_test])

def _extract_X(X_train, X_test):
    vectorizer, X_train = _build_vectorizer(X_train)
    X_test = _test_to_vector(X_test, vectorizer)
    return X_train, X_test

def _build_dict(y_train):
    y_dict = {}
    for y in y_train:
        if y not in y_dict:
            y_dict[y] = len(y_dict)
    return y_dict

def _extract_y(y_train, y_test):
    y_dict = _build_dict(y_train)
    y_train = [y_dict[y] for y in y_train]
    y_test = [y_dict[y] for y in y_test]
    return y_train, y_test

def extract_data():
    y, urls, articles = load_data('data/y','data/urls','data/articles')
    y, urls, articles = shuffle(y, urls, articles, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(articles, y, test_size=0.1, random_state=0)
    X_train, X_test = _extract_X(X_train, X_test)
    y_train, y_test = _extract_y(y_train, y_test)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    main()


# vectorizer = CountVectorizer(min_df=1)
# bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)
# vectorizer = TfidfVectorizer(min_df=1)
# vectorizer.fit_transform(corpus)
