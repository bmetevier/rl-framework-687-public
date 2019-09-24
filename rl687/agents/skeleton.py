from abc import ABC, abstractmethod


class Agent(ABC):
    """
    A reinforcement learning agent. 

    A reinforcement learning Agent learns a decision-making policy by 
    interacting with an Environment. In general,the Agent's goal is to maximize
    the reward signal (specifically, the discounted sum of rewards) it receives
    from interacting with the Environment. 
    """

    @property
    @abstractmethod
    def name(self):
        """The agent name."""
        pass

    @abstractmethod
    def reset(self):
        """
        Alerts the agent that the episode or iteration of interest has
        ended and it should prepare for the next one. 
        """
        pass