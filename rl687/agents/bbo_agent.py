from abc import ABC, abstractmethod
from .skeleton import Agent


class BBOAgent(Agent):
    """
    An Agent that employs black box optimization techniques.
    """

    @property
    @abstractmethod
    def parameters(self):
        """
        The best policy parameters the agent has found. This should be a 1D
        numpy array.
        """
        pass
    
    @abstractmethod
    def train(self):
        """
        Perform a single iteration of the BBO algorithm. For example, this 
        means performing a single iteration of the while loop of the CEM 
        pseudocode located in the class notes. 
        
        output:
            bestParameter -- the best parameter found during the training iteration.
                        This will NOT necessarily be the overall best parameterized 
                        policy found. 
        """
        pass