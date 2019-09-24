import numpy as np
from typing import Tuple
from .skeleton import Environment


class Cartpole(Environment):
    """
    The cart-pole environment as described in the 687 course material. This
    domain is modeled as a pole balancing on a cart. The agent must learn to
    move the cart forwards and backwards to keep the pole from falling.

    Actions: left (0) and right (1)
    Reward: 1 always

    Environment Dynamics: See the work of Florian 2007
    (Correct equations for the dynamics of the cart-pole system) for the
    observation of the correct dynamics.
    """

    def __init__(self):
        # TODO: properly define the variables below
        self._name = "???"
        self._action = 0
        self._reward = 0
        self._isEnd = 0
        self._gamma = 0.0

        # define the state # NOTE: you must use these variable names
        self._x = 0.  # horizontal position of cart
        self._v = 0.  # horizontal velocity of the cart
        self._theta = 0.  # angle of the pole
        self._dtheta = 0.  # angular velocity of the pole

        # dynamics
        self._g = 0.0  # gravitational acceleration (m/s^2)
        self._mp = 0.0  # pole mass
        self._mc = 0.0  # cart mass
        self._l = 0.0  # (1/2) * pole length
        self._dt = 0.0  # timestep
        self._t = 0.0  # total time elapsed  NOTE: USE must use this variable

    @property
    def name(self) -> str:
        # TODO
        pass

    @property
    def reward(self) -> float:
        # TODO
        pass

    @property
    def gamma(self) -> float:
        # TODO
        pass

    @property
    def action(self) -> int:
        # TODO
        pass

    @property
    def isEnd(self) -> bool:
        # TODO
        pass

    @property
    def state(self) -> np.ndarray:
        # TODO
        pass

    def nextState(self, state: np.ndarray, action: int) -> np.ndarray:
        """
        Compute the next state of the pendulum using the euler approximation to the dynamics
        """
        # TODO
        pass

    def R(self, state: np.ndarray, action: int, nextState: np.ndarray) -> float:
        # TODO
        pass

    def step(self, action: int) -> Tuple[np.ndarray, float, bool]:
        """
        takes one step in the environment and returns the next state, reward, and if it is in the terminal state
        """
        # TODO
        pass

    def reset(self) -> None:
        """
        resets the state of the environment to the initial configuration
        """
        # TODO
        pass

    def terminal(self) -> bool:
        """
        The episode is at an end if:
            time is greater that 20 seconds
            pole falls |theta| > (pi/12.0)
            cart hits the sides |x| >= 3
        """
        # TODO
        pass
