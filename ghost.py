#!/usr/bin/env python
import random
import numpy as np
from emotions import Emotion
from textblob import TextBlob
from word import Word, Words
import text2emotion as te
import markovify

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
        self.sentences = []
        self.words = Words(self.feeling, self.opposite)
        self.markov_blob = None

    # def get_power_words(self):
    #     new_set = []
    #     for word in self.words:
    #         if word.type == "Power": 
    #             new_set.append(word)
    #     return new_set

    # def get_opposite_words(self):
    #     return np.select([self.words.type == "Obstacle"],self.words)

    # def get_other_words(self):
    #     return np.select([self.words.type == "Null"], self.words)

    # def get_power(self):
    #     return np.sum(self.get_power_words().power)

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
            return story, 'DONE'

        # otherwise start reading until either the story is over or you've read your read rate
        # Get chunk starting at start_word and read
        for i in range(start_sentence, start_sentence + self.read_rate):
            if(i < len(story.sentences)):
                story.sentences[i] = self.parse_sentence(story.sentences[i])

        #self.write(story, story.text)

        # If still reading, return READING, otherwise, return DONE
        if(start_sentence + self.read_rate >= len(story.sentences)):
            return story, 'DONE'
        else:
            return story, 'READING'

    def parse_sentence(self, sentence):
        emotion_analysis = te.get_emotion(str(sentence))
        if emotion_analysis[self.opposite] > emotion_analysis[self.feeling]:
            # Re write it
            sentence = self.rewrite(sentence) 
        elif emotion_analysis[self.feeling] > emotion_analysis[self.opposite]:
            # Take its words
            #self.words_markov = markovify.combine([self.words_markov,markovify.Text(str(sentence))],[1,1])
            self.sentences.append(str(sentence))
            self.markov_blob = markovify.Text(self.sentences)
            for word in sentence.words:
                #self.words.append(Word(word,te.get_emotion(word),self.feeling,self.opposite))
                self.words.add_word(word)

        #for word in word_bag:
            #if word == self.SCREAM:
                # power surge?

        return sentence

    def rewrite(self, sentence):
        if(self.markov_blob == None):
            return sentence
        emotion_analysis = te.get_emotion(str(sentence))
        #b.sentence = 
        #used_words = []
        #words_to_use = self.get_power_words().copy()
        #no_power = False

        i = 0
        #while emotion_analysis[self.opposite] >= emotion_analysis[self.feeling] and not no_power:
        while emotion_analysis[self.opposite] >= emotion_analysis[self.feeling] and i < 5:
            used_words = []
            #words_to_use = self.get_power_words().copy()
            # Change the sentence
            
            test_sentence = self.markov_blob.make_short_sentence(len(str(sentence)))
            if(test_sentence != None):
                print("------------")
                print("Original Sentence: " + str(sentence))
                print("Test Sentence: " + test_sentence, flush=True)
                emotion_analysis = te.get_emotion(test_sentence)
                if(emotion_analysis[self.opposite] < emotion_analysis[self.feeling]):
                    new_blob = TextBlob(test_sentence)
                    if(self.words.has_words(new_blob.sentences[0].words)):
                        sentence = new_blob.sentences[0]
                        self.words.remove_words(new_blob.sentences[0].words)
                        i = 5
            else:
                i = 5

            i += 1
            # Remove negative words? Find markovify fits for good words?
            # Tell it to just change words until it gets a good score set?
            # for word in sentence.words:
            #     pos, neg = self.parse_word(word)
            #     if(neg > pos):
            #         if len(words_to_use) > 0:
            #             new = random.choice(words_to_use)
            #             words_to_use.remove(new)
            #             used_words.append(new)
            #             word = new
            #     if len(words_to_use) < 1:
            #         no_power = True
            #         used_words = []
            #         break
            #emotion_analysis = te.get_emotion(str(sentence))


        #if(i < 5 or (emotion_analysis[self.opposite] < emotion_analysis[self.feeling])):


        # Remove all the words we used
        #for word in used_words:
        #    self.words.remove(word)

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