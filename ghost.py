#!/usr/bin/env python
import random

'''
Ghost class definition, includes the ghost emotion, ghost antithetical emotion, the ghost's current collection of words, and handling of ghost choices
'''
class Ghost:
    def __init__(self, emotion):
        self.emotion = emotion
        #self.anti = anti
        self.read_rate = random.randint(3,50) # number of words to read
        self.current_power = random.randint(0,30) # starting power?
        self.words = []

    
    def read(self,story,timestep):
        # Get the story text
        f = open(story, "r")
        text = f.read()
        f.close()

        # Get the current state of the story and read where the ghost is in the story at it's read rate
        start_word = timestep*self.read_rate
        # Check that the start word isn't greater than the number of words
        # if it is then you're done

        #otherwise start reading until either the story is over or you've read your read rate
        

        # If still reading, return READING, otherwise, return DONE
        return 'READING'

    def write(self, story, text):
        f.open(story, "w")
        f.write(text)
        f.close()