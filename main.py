#!/usr/bin/env python
from ghost import Ghost
from emotions import Emotion
import random
import numpy as np
from textblob import TextBlob

def main(STORY = './story.txt'):
    '''
    Handles global state, reading and writing of the story, and definition of each ghost.
    '''
    NUM_GHOSTS = 5

    f = open(STORY, "r")
    text_blob_object = TextBlob(f.read())
    
    f.close()

    # Create a bunch of ghosties
    ghosties = []
    for i in range(NUM_GHOSTS):
        ghosties.append(Ghost())
    
    timestep = 0
    all_finished = False
    # Loop until all ghosts have finished with the story
    while not all_finished:
        all_finished = True
        for ghosty in ghosties:
            text_blob_object, status = ghosty.read(text_blob_object,timestep)
            if status is not 'DONE':
                all_finished = False
        timestep += 1

    print('Finished ghost reading time at timestep ' + str(timestep))
    f = open("./new.txt","w")
    f.write(str(text_blob_object))
    f.close()



if __name__ == "__main__":
    import sys

    # Get the story file
    if len(sys.argv) > 1:
        story = str(sys.argv[1])
        main(story)
    else:
        main()

    

