from random import sample, random
import numpy as np
from random import choice

def mutation_sample(indiv,number_mut):
    """
    """

    indexes_mut = sample(indiv.index_missing, k=number_mut) # used sample instead of choices because of the non 'replacement' factor

    for i in indexes_mut:
        indiv[i] = sample(indiv.valid_set, k=1)

    return indiv

def mutation_prob(indiv):
    """
    """
    for i in indiv.index_missing:
        if random() < prob:
            indiv[i] = sample(indiv.valid_set, k=1)
    return indiv

def mutation_swap(indiv):
    ## do column and box
    """
    """


    ind_chosen = choice(0, 9)*9
    missing_row = indiv.index_missing[ind_chosen:ind_chosen+9]

    choose_2 = choice(missing_row, 2)
    indiv_orig = indiv.deepcopy()
    indiv[choose_2[0]] = indiv[choose_2[1]]
    indiv[choose_2[1]] = indiv_orig[choose_2[0]]

    return indiv