import numpy as np
from .bbo_agent import BBOAgent

from typing import Callable


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
    initPopulationFunction (function): creates the first generation of
                    individuals to be used for the GA
        input: populationSize (int)
        output: a numpy matrix of size (N x M) where N is the number of 
                individuals in the population and M is the number of 
                parameters (size of the parameter vector)
    numElite (int): the number of top individuals from the current generation
                    to be copied (unmodified) to the next generation
    
    """

    def __init__(self, populationSize:int, evaluationFunction:Callable, 
                 initPopulationFunction:Callable, numElite:int=1, numEpisodes:int=10):
        #TODO
        pass

    @property
    def name(self)->str:
        #TODO
        pass
    
    @property
    def parameters(self)->np.ndarray:
        #TODO
        pass

    def _mutate(self, parent:np.ndarray)->np.ndarray:
        """
        Perform a mutation operation to create a child for the next generation.
        The parent must remain unmodified. 
        
        output:
            child -- a mutated copy of the parent
        """
        
        #TODO
        pass

    def train(self)->np.ndarray:
        #TODO
        pass

    def reset(self)->None:
        #TODO
        pass