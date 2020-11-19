#!/usr/bin/env python
import random
import numpy as np
from emotions import Emotion
from textblob import TextBlob
from word import Word
import text2emotion as te

'''
Ghost class definition, includes the ghost emotion, ghost antithetical emotion, the ghost's current collection of words, and handling of ghost choices
'''
class Ghost:
    def __init__(self):
        emotion_list = ["Angry", "Fear", "Happy", "Sad", "Surprise"]
        self.feeling = random.choice(emotion_list)
        emotion_list.remove(self.feeling)
        self.opposite = random.choice(emotion_list)
        self.read_rate = random.randint(1,10) # number of sentences to read
        #self.current_power = random.randint(0,30) # starting power?
        self.words = []

    def get_power_words(self):
        new_set = []
        for word in self.words:
            if word.type == "Power": 
                new_set.append(word)
        return new_set

    def get_opposite_words(self):
        return np.select([self.words.type == "Obstacle"],self.words)

    def get_other_words(self):
        return np.select([self.words.type == "Null"], self.words)

    def get_power(self):
        return np.sum(self.get_power_words().power)

    def read(self,story,timestep):
        # Get the story text
        #f = open(story, "r")
        #text_blob_object = TextBlob(f.read())
        #f.close()

        # Get the current state of the story and read where the ghost is in the story at it's read rate
        start_sentence = timestep*self.read_rate

        # Check that the start word isn't greater than the number of sentences
        # if it is then you're done
        if(len(story.sentences) < start_sentence):
            return 'DONE'

        # otherwise start reading until either the story is over or you've read your read rate
        # Get chunk starting at start_word and read
        for i in range(start_sentence, start_sentence + self.read_rate):
            if(i < len(story.sentences)):
                story.sentences[i] = self.parse_sentence(story.sentences[i])

        #self.write(story, story.text)

        # If still reading, return READING, otherwise, return DONE
        if(start_sentence + self.read_rate >= len(story.sentences)):
            return 'DONE'
        else:
            return 'READING'

    def parse_sentence(self, sentence):
        emotion_analysis = te.get_emotion(str(sentence))
        if emotion_analysis[self.opposite] > emotion_analysis[self.feeling]:
            # Re write it
            sentence = self.rewrite(sentence) 
        elif emotion_analysis[self.feeling] > emotion_analysis[self.opposite]:
            # Take its words
            for word in sentence.words:
                self.words.append(Word(word,te.get_emotion(word),self.feeling,self.opposite))

        #for word in word_bag:
            #if word == self.SCREAM:
                # power surge?

        return sentence

    def rewrite(self, sentence):
        emotion_analysis = te.get_emotion(str(sentence))
        #b.sentence = 
        used_words = []
        words_to_use = self.get_power_words().copy()
        no_power = False
        while emotion_analysis[self.opposite] >= emotion_analysis[self.feeling] and not no_power:
            used_words = []
            words_to_use = self.get_power_words().copy()
            # Change the sentence
            # Remove negative words? Find markovify fits for good words?
            # Tell it to just change words until it gets a good score set?
            for word in sentence.words:
                pos, neg = self.parse_word(word)
                if(neg > pos):
                    if len(words_to_use) > 0:
                        new = random.choice(words_to_use)
                        words_to_use.remove(new)
                        used_words.append(new)
                        word = new
                if len(words_to_use) < 1:
                    no_power = True
                    used_words = []
                    break
            emotion_analysis = te.get_emotion(str(sentence))


        # Remove all the words we used
        for word in used_words:
            self.words.remove(word)

        return sentence


    def parse_word(self,word):
        analyse = te.get_emotion(word)
        positive = analyse[self.feeling]
        negative = analyse[self.opposite]
        return positive, negative


    def write(self, story, text):
        f.open(story, "w")
        f.write(text)
        f.close()