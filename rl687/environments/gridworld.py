import numpy as np
from typing import Tuple
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

    def __init__(self, startState=0, endState=24, shape=(5, 5), obstacles=(12, 17), waterStates=(6, 18, 22)):
        self._name = "Gridworld"
        self._gamma = 0.9
        self._startState = startState
        self._endState = endState
        self._waterStates = waterStates
        self._obstacles = obstacles

        self._state = self._startState
        self._action = None
        self._reward = 0
        self._isEnd = False

        self._shape = tuple(shape)
        self._size = self._shape[0] * self._shape[1]
        self._R = self._initR()  # dict mapping states to rewards

        # define stochasticity
        self._prStay = 0.1
        self._prRotate = 0.05
        # dicts mapping actions to the appropriate rotations
        self._rotateLeft = {0: 2, 1: 3, 2: 1, 3: 0}
        self._rotateRight = {0: 3, 1: 2, 2: 0, 3: 1}

    @property
    def name(self) -> str:
        return self._name

    @property
    def reward(self) -> float:
        return self._reward

    @property
    def action(self) -> int:
        return self._action

    @property
    def isEnd(self) -> bool:
        return self._isEnd

    @property
    def state(self) -> int:
        # return int(np.where(x==1)[0])
        return int(self._state)

    @property
    def gamma(self) -> float:
        return self._gamma

    def nextState(self, state: int, action: int) -> int:

        if state == self._endState:
            return state

        noise = np.random.uniform()
        if noise < self._prStay:  # do nothing
            return state
        elif noise < (self._prStay + self._prRotate):
            action = self._rotateLeft[action]
        elif noise < (self._prStay + 2 * self._prRotate):
            action = self._rotateRight[action]

        # simulate taking a step in the environment
        nextState = self._state
        if action == 0:  # move up
            nextState = state - self._shape[1]
        elif action == 1:  # move down
            nextState = state + self._shape[1]
        elif action == 2 and (nextState % self._shape[1] != 0):  # move left
            nextState = state - 1
        elif action == 3 and ((nextState + 1) % self._shape[1] != 0):  # move right
            nextState = state + 1

        if nextState >= 0 and nextState < self._size and nextState not in self._obstacles:
            return nextState
        else:
            return state

    def step(self, action: int) -> Tuple[int, float, bool]:

        nextState = self.nextState(self._state, action)
        self._reward = self.R(int(self._state), action, nextState)
        self._state = nextState
        self._isEnd = self._state == self._endState

        return self.state, self.reward, self.isEnd

    def reset(self) -> None:
        self._state = self._startState
        self._action = None
        self._reward = 0
        self._isEnd = False

    def _initR(self) -> dict:
        """
        Initialize the reward function.

        output:
            rdict -- a dictionary mapping integer states to reward values
        """
        rdict = {i: 0 for i in range(0, self._size)}
        rdict[self._endState] = 10
        for w in self._waterStates: rdict[w] = -10
        for o in self._obstacles: rdict[o] = None

        return rdict

    def R(self, state: int, action: int, nextState: int) -> float:
        return 0 if (state == nextState and nextState == self._endState) else self._R[nextState]
