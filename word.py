#!/usr/bin/env python
from emotions import Emotion

class Word:
    def __init__(self, word, emotion, power):
        self.id = word
        self.feeling = emotion
        self.power = power