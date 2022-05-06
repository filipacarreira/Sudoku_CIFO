from random import choice, sample, random
import numpy as np
from copy import deepcopy

def uniform_co_alt(indiv1, indiv2, prob_co=0.2): #took into consideration not changing the numbers given

    """

    """

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    for elem in (set(indiv1.index_missing) and set(indiv2.index_missing)):

        if random() < prob_co:
            offspring1[elem] = indiv2[elem]
            offspring2[elem] = indiv1[elem]

    return offspring1, offspring2

def uniform_co(indiv1, indiv2, prob_co=0.7):

    """

    """

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    for elem in range(len(indiv1)):
        if random() < prob_co:
            offspring1[elem] = indiv2[elem]
            offspring2[elem] = indiv1[elem]

    return offspring1, offspring2

