from abc import ABC, abstractmethod

class Environment(ABC):
    """
    A reinforcement learning environment. 
    
    The Environment defines everything outside of the Agent, including 
    the states, actions, transitions between states, and rewards. In general,
    an agent's goal is to maximize the reward signal received from the 
    environment.

    """

    @property
    @abstractmethod
    def name(self):
        """The environment name."""
        pass

    @property
    @abstractmethod
    def reward(self):
        """
        The reward resulting from taking the last action
        in the environment."""
        pass

    @property
    @abstractmethod
    def action(self):
        """
        The last action taken in the environment.
        """
        pass

    @property
    @abstractmethod
    def isEnd(self):
        """
        True if the environment needs to be reset and False
        otherwise.
        """
        pass

    @property
    @abstractmethod
    def state(self):
        """
        The current state of the environment.
        """
        pass

    @property
    @abstractmethod
    def gamma(self):
        """
        The reward discount factor.
        """
        pass

    @abstractmethod
    def step(self, action):
        """
        An action is taken in the environment and the next
        state is entered.

        output: 
            state -- the next state
            reward -- the reward from taking the action
            isEnd -- True if environment reset is required
        """
        pass

    @abstractmethod
    def reset(self):
        """
        The environment is reset.
        """
        pass



