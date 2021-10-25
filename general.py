import re   # For regular expressions
import os
# BeautifulSoup is used to parse the HTML
from bs4 import BeautifulSoup

# import nltk
# nltk.download('stopwords','model')
# nltk.download('wordnet')

# from nltk.corpus import stopwords

import pickle

model = pickle.load(open(os.path.join("model","model.pkl"),"rb"))
vectorizer = pickle.load(open(os.path.join("model","vectorizer.pkl"),"rb"))




def review_to_word(review, remove_stopwords=False):
    # Function to convert raw review to string of words,
    # optionally removing stop words.  
    # Returns string of words.
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(review, features="html.parser").get_text()
    
    # 2. Remove non-letters (all punctuation, and all whitespace)
    review_text = re.sub("'","",review_text)
    review_text = re.sub("[^a-zA-Z]"," ", review_text)

    # 3. Convert words to lower case and split them
    words = review_text.lower().split()
    
    # 4. Optionally remove stop words (false by default)
    # if remove_stopwords:
    #     stops = set(stopwords.words("english"))
    #     words = [w for w in words if not w in stops]
    
    # 5. Return a string of words
    return(" ".join(words))

def movie_sentiment(review):
    clean_review = []
    clean_review.append(review_to_word(review,remove_stopwords=False))
    clean_review = vectorizer.transform(clean_review)
    clean_review = clean_review.toarray()

    # predicting
    pred = model.predict(clean_review)
    return pred[0]
