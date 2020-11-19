#!/usr/bin/env python
from emotions import Emotion

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