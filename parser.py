#!/usr/bin/env python
#import nltk
#nltk.download('wordnet')
#from senti_classifier import senti_classifier
from textblob import TextBlob
import text2emotion as te

'''
Word/sentence parsers for determining the power and emotion of words and statements
'''

def get_sentence_value(sentence):
    sentiment_analysis = TextBlob(sentence).sentiment
    emotion_analysis = te.get_emotion(sentence)

    power = 0

    return emotion, power

def get_word_value(word):
    emotion_analysis = te.get_emotion(sentence)
    #emotion = 
    power = 0

    return emotion, power