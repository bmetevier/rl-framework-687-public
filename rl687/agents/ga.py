import numpy as np
from .bbo_agent import BBOAgent

class GA(BBOAgent):
    """
    A canonical Genetic Algorithm (GA) for policy search is a black box 
    optimization (BBO) algorithm. 
    
    Parameters
    ----------
    populationSize (int): the number of individuals per generation
    numEpisodes (int): the number of episodes to sample per policy         
    evaluationFunction (function): evaluates a parameterized policy
        input: a parameterized policy theta, numEpisodes
        output: the estimated return of the policy            
    numElite (int): the number of top individuals from the current generation
                    to be copied (unmodified) to the next generation
    """

    def __init__(self, populationSize, evaluationFunction, numElite=1, numEpisodes=10):
        #TODO
        pass

    @property
    def name(self):
        #TODO
        pass
    
    @property
    def parameters(self):
        #TODO
        pass

    def _mutate(self, parent:np.ndarray):
        """
        Perform a mutation operation to create a child for the next generation.
        The parent must remain unmodified. 
        
        output:
            child -- a mutated copy of the parent
        """
        
        #TODO
        pass

    def train(self):
        #TODO
        pass

    def reset(self):
        #TODO
        pass