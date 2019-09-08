import numpy as np
from .skeleton import Environment

class Gridworld(Environment):
    """
    The Gridworld as described in the lecture notes of the 687 course material. 
    
    Actions: up (0), down (1), left (2), right (3)
    
    Environment Dynamics: With probability 0.8 the robot moves in the specified
        direction. With probability 0.05 it gets confused and veers to the
        right -- it moves +90 degrees from where it attempted to move, e.g., 
        with probability 0.05, moving up will result in the robot moving right.
        With probability 0.05 it gets confused and veers to the left -- moves
        -90 degrees from where it attempted to move, e.g., with probability 
        0.05, moving right will result in the robot moving down. With 
        probability 0.1 the robot temporarily breaks and does not move at all. 
        If the movement defined by these dynamics would cause the agent to 
        exit the grid (e.g., move up when next to the top wall), then the
        agent does not move. The robot starts in the top left corner, and the 
        process ends in the bottom right corner.
        
    Rewards: -10 for entering the state with water
            +10 for entering the goal state
            0 everywhere else
        
    
    
    """

    def __init__(self, startState=0, endState=24, shape=(5,5), obstacles=[12, 17], waterStates=[6, 18, 22]):
        pass
        
    @property
    def name(self):
        pass
        
    @property
    def reward(self):
        pass

    @property
    def action(self):
        pass

    @property
    def isEnd(self):
        pass

    @property
    def state(self):
        pass

    @property
    def gamma(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass
        
    def R(self, _state):
        """
        reward function
        
        output:
            reward -- the reward resulting in the agent being in a particular state
        """
        pass
