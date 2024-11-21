import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def stemming(row):
    ps = PorterStemmer()
    tokens = word_tokenize(row)
    return ' '.join([ps.stem(word) for word in tokens])