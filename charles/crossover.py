from random import choice, sample, random
import numpy as np
from copy import deepcopy

def uniform_co_alt(indiv1, indiv2, prob_co=0.2): #took into consideration not changing the numbers given

    """

    """

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    for elem in (set(indiv1.index_missing) and set(indiv2.index_missing)):

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

def cross_no(indiv1, indiv2):

    """

    """

    return indiv1, indiv2

def swap_lines(indiv1, indiv2):

    random_decision = sample(range(0, 3), k=1)[0]

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    if random_decision == 0:  # do crossover by rows
        choice_row = sample([0, 9], k=1)[0]
        choice_row = choice_row

        offspring1[choice_row:choice_row+9] = indiv2[choice_row:choice_row+9]
        offspring2[choice_row:choice_row+9] = indiv1[choice_row:choice_row+9]

    elif random_decision == 1:  # do crossover by columns
        ind_chosen = sample(range(0, 9), k=1)[0]
        #print([ind_chosen + (i * 9) for i in range(0, 9)])
        ind_column = [ind_chosen + (i * 9) for i in range(0, 9)]

        for ind in ind_column:
            offspring1[ind] = indiv2[ind]
            offspring2[ind] = indiv1[ind]

    elif random_decision == 2:  # do crossover by boxs

        block_chosen = sample(range(0, 3), k=1)[0]
        box_chosen = sample(range(0, 3), k=1)[0]
        ind_initial = block_chosen * 27 + box_chosen * 3

        for k in range(0, 3):  # 3 lines

            ind_box = []

            ind_box = [ind_initial + i + k * 9 for i in range(0, 3)]

            for ind in ind_box:
                offspring1[ind] = indiv2[ind]
                offspring2[ind] = indiv1[ind]

    return offspring1, offspring2

