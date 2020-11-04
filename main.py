#!/usr/bin/env python
from ghost import Ghost
from emotions import Emotion
import random
import numpy as np

'''
Handles global state, reading and writing of the story, and definition of each ghost.
'''
NUM_GHOSTS = 50
STORY = './story.txt'


if __name__ == "__main__":
    import sys

    # Get the story file
    if len(sys.argv) > 1:
        STORY = str(sys.argv[1])

    # Create a bunch of ghosties
    ghosties = []
    for i in range(NUM_GHOSTS):
        # Pick an emotion for the ghostie
        emotion = random.choice(list(Emotion))
        ghosties.append(Ghost(emotion))
    
    timestep = 0
    all_finished = False
    # Loop until all ghosts have finished with the story
    while not all_finished:
        all_finished = True
        for ghosty in ghosties:
            status = ghosty.read(STORY,timestep)
            if status is not 'DONE':
                all_finished = False
        timestep += 1

    print('Finished ghost reading time at timestep ' + str(timestep))

