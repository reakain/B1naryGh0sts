#!/usr/bin/env python
from emotions import Emotion
import text2emotion as te

class Word:
    def __init__(self, word, result, emotion, opposite):
        self.id = word
        self.type = ''
        if result[emotion] > 0.0 and result[opposite] < result[emotion]:
            self.type = "Power"
            self.power = result[emotion]
        elif result[opposite] > 0.0:
            self.type = "Obstacle"
            self.power = result[opposite]
        else:
            self.type = "Null"
            self.power = 0.0

class Words:
    def __init__(self, feeling, opposite):
        self.word_list = []
        self.feeling = feeling
        self.opposite = opposite

    def add_word(self, id):
        self.word_list.append(Word(id,te.get_emotion(id),self.feeling,self.opposite))

    def get_power_words(self):
        new_set = []
        for word in self.word_list:
            if word.type == "Power": 
                new_set.append(word)
        return new_set

    def get_power(self):
        return np.sum(self.get_power_words().power)

    def has_word(self, id, word_list = None):
        if word_list == None:
            word_list = self.word_list
        for word in word_list:
            if word.id == id: 
                return True
    
    def get_word(self, id, word_list = None):
        if word_list == None:
            word_list = self.word_list
        for word in word_list:
            if word.id == id: 
                return word
        return None

    def remove_word(self, id):
        for word in self.word_list:
            if word.id == id:
                self.word_list.remove(word)
                return

    def remove_words(self, words):
        if(self.has_words(words)):
            for word in words:
                self.remove_word(word)
            return True
        else:
            return False


    def has_words(self, words):
        test_list = self.word_list.copy()
        for word in words:
            word_get = self.get_word(word, test_list)
            if(word_get != None):
                test_list.remove(word_get)
            else:
                return False
        return True

