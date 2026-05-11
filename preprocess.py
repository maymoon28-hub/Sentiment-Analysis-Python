# Placeholder for preprocess.py

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def get_revised_stopwords():
    revised_stopwords = set(stopwords.words("english"))
    negative_words = {'no', 'not', 'don', "don't", 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 
    'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'mightn', "mightn't", 'mustn', 
    "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', 
    "weren't", 'won', "won't", 'wouldn', "wouldn't", 'nor', 'never', 'nothing','very', 'more', 'most', 'just', 'too', 'only', 'so', 'pretty','but','all', 'any', 'none', 'nothing', 'some' }
    revised_stopwords.difference_update(negative_words)
    return revised_stopwords
    
def preprocess(row):
    if not isinstance(row, str):
        return ""
        
    tokens=row.lower().split() #splits each row into words
    revised_filtered = " ".join([word for word in tokens if word not in get_revised_stopwords()])
    #print(idx+1,"comment:" ,rows)
    return revised_filtered


    