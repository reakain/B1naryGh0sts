#!/usr/bin/env python
import random
import numpy as np
from emotions import Emotion
from textblob import TextBlob
from word import Word

'''
Ghost class definition, includes the ghost emotion, ghost antithetical emotion, the ghost's current collection of words, and handling of ghost choices
'''
class Ghost:
    def __init__(self, emotion):
        self.feeling = emotion
        if( (emotion.value % 2) == 0):
            # even
            self.opposite = emotion.value + 1
        else:
            # odd
            self.opposite = emotion.value - 1
        self.read_rate = random.randint(3,50) # number of words to read
        #self.current_power = random.randint(0,30) # starting power?
        self.words = []

    def get_power_words(self):
        return np.select([self.words.feeling == self.feeling],self.words)

    def get_null_words(self):
        return np.select([self.words.feeling != self.feeling],self.words)

    def get_power(self):
        return np.sum(self.get_power_words().power)

    def read(self,story,timestep):
        # Get the story text
        f = open(story, "r")
        text_blob_object = TextBlob(f.read())
        f.close()

        # Get the current state of the story and read where the ghost is in the story at it's read rate
        start_word = timestep*self.read_rate

        # Check that the start word isn't greater than the number of words
        # if it is then you're done
        if(len(text_blob_object.words) < start_word):
            return 'DONE'

        # otherwise start reading until either the story is over or you've read your read rate
        # Get chunk starting at start_word and read
        for i in range(start_word, start_word + self.read_rate):
            if(i < len(text_blob_object.words)):
                self.parse_word(text_blob_object.words[i])

        # If still reading, return READING, otherwise, return DONE
        if(start_word + self.read_rate >= len(text_blob_object.words)):
            return 'DONE'
        else:
            return 'READING'

    def parse_word(self,word):
        # get emotion + power
        emotion = None
        if(emotion == None):
            self.words.append(Word(word,emotion,0))
        elif(emotion == self.feeling):
            self.words.append(Word(word,emotion,0))
        elif(emotion == self.opposite):
            self.words.append(Word(word,emotion,0))


    def write(self, story, text):
        f.open(story, "w")
        f.write(text)
        f.close()