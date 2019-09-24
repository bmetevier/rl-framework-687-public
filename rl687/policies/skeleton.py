from abc import ABC, abstractmethod


class Policy(ABC):
    """
    A reinforcement learning policy.
    
    A Policy is a decision-making rule in reinforcement learning. An Agent 
    can use a Policy to select actions to take in an environment. 

    """

    @abstractmethod
    def __call__(self, state, action=None):
        """
        Provides the probability of taking an action in a given state. If no
        action is supplied, the probability distribution over actions is 
        provided. 
       
        output:
            probabilities -- the probability of taking an action in the state
                                provided OR the probability distribution over
                                actions for the state provided
        """
        pass
