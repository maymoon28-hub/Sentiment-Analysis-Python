# Placeholder for analyse.py

import nltk
nltk.download('punkt')
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer



def label_from_compound(c):
    if c>=0.05: return "positive"
    if c<=-0.05: return "negative"
    return "neutral"

def analyse(revised_filtered):
    sia=SentimentIntensityAnalyzer()
    revised_sentiment = sia.polarity_scores(revised_filtered)["compound"]
    
    compound_score=label_from_compound(sia.polarity_scores(revised_filtered)["compound"])
    return compound_score

    

