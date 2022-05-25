from random import choice, sample, random, uniform, randint
from copy import deepcopy

def in_common_co (indiv1, indiv2): #took into consideration not changing the numbers given

    """
    Implementation of In Common Crossover - created by us specifically for the sudoku problem.
    Considering only the indexes of individuals that are not in the initial game either for the first individual or for the second.
    We 9 random common indexes.

    Args:
        indiv1 (Individual): First parent for crossover.
        indiv2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.

    """

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    # for the two individuals we check which are the common missing indexes (indexes that aren't present in the initial puzzle)
    # for 9 out of these indexes we swap the numbers from one individual to the other.

    elem = choice(indiv1.index_missing, k=9)[0]
    offspring1[elem] = indiv2[elem]
    offspring2[elem] = indiv1[elem]

    return offspring1, offspring2

def in_common_prob_co(indiv1, indiv2, prob_co=0.7):

    """
    Implementation of In Common Crossover Probability - created by us specifically for the sudoku problem.
    Similar to the Common Crossover defined above, except that here we consider a probability to apply this crossover for each common index.

    Args:
        indiv1 (Individual): First parent for crossover.
        indiv2 (Individual): Second parent for crossover.
        prob_co : probability that defines the amount of time we are applying the crossover

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    # for the two individuals we check which are the common indexes missing (indexes that aren't present in the initial puzzle)
    # for all of these indexes we swap the numbers from one individual to the other
    # additionally, we check if the probability is smaller than the one given, so that we only apply this crossover prob_co% of the times

    for elem in indiv1.index_missing:
        if random() < prob_co:
            offspring1[elem] = indiv2[elem]
            offspring2[elem] = indiv1[elem]

    return offspring1, offspring2


def swap_elements_co(indiv1, indiv2):
    """
    Implementation of Swap Elements Crossover - created by us specifically for the sudoku problem
    Randomly chose if the crossover is applied to columns, rows or boxes
    After choosing the "variable" to use, we just choose 2 individuals to swap from the correspondent row, column or box between each other
    This crossover method takes into account that we can't change the numbers that were already in the initial puzzle
    (if we swap the first row, for example, in one individual with the same row of another individual, the original numbers are the same)

    Args:
        indiv1 (Individual): First parent for crossover.
        indiv2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Choosing which "variable" to swap
    # 0 = Swapping rows
    # 1 = Swapping columns
    # 3 = Swapping boxes
    random_decision = sample(range(0, 3), k=1)[0]

    offspring1 = deepcopy(indiv1)
    offspring2 = deepcopy(indiv2)

    if random_decision == 0:  # do crossover by rows
        # We choose a random row to swap
        choice_row = sample([0, 9], k=1)[0]
        choice_row = choice_row

        # The selected row of the first individual is the selected row of the second individual
        # and the selected row of the second individual is the selected row of the first individual
        offspring1[choice_row:choice_row+9] = indiv2[choice_row:choice_row+9]
        offspring2[choice_row:choice_row+9] = indiv1[choice_row:choice_row+9]

    elif random_decision == 1:  # do crossover by columns
        # We choose a random column to swap
        ind_chosen = sample(range(0, 9), k=1)[0]
        #print([ind_chosen + (i * 9) for i in range(0, 9)])

        # Saving the indexes of the column
        ind_column = [ind_chosen + (i * 9) for i in range(0, 9)]

        # The selected column of the first individual is the selected row of the second individual
        # and the selected column of the second individual is the selected row of the first individual
        for ind in ind_column:
            offspring1[ind] = indiv2[ind]
            offspring2[ind] = indiv1[ind]

    elif random_decision == 2:  # do crossover by boxs
        # Choosing a random block
        # A block is a set of 3 boxes 3*3 (so basically indicates the 3 boxes in the first rows of the sudoku)
        block_chosen = sample(range(0, 3), k=1)[0]

        # Inside the block, choose a random box to swap
        box_chosen = sample(range(0, 3), k=1)[0]

        # Saving the initial index of the box chosen
        ind_initial = block_chosen * 27 + box_chosen * 3

        for k in range(0, 3):  # 3 lines

            ind_box = []

            # saving the indexes of the box
            ind_box = [ind_initial + i + k * 9 for i in range(0, 3)]

            # The selected box of the first individual is the selected row of the second individual
            # and the selected box of the second individual is the selected row of the first individual
            for ind in ind_box:
                offspring1[ind] = indiv2[ind]
                offspring2[ind] = indiv1[ind]

    return offspring1, offspring2


## NOT USED - The methods under did not make sense in the context of our problem
#             since we have to take into account the numbers present in the initial puzzle

def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2


def cycle_co(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p2)
    # While there are still None values in offspring, get the first index of
    # None and start a "cycle" according to the cycle crossover method
    while None in offspring1:
        index = offspring1.index(None)

        val1 = p1[index]
        val2 = p2[index]

        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    return offspring1, offspring2


def pmx_co(p1, p2):
    """Implementation of partially matched/mapped crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_points = sample(range(len(p1)), 2)
    co_points.sort()

    # dictionary creation using the segment elements from both parents
    # the dictionary will be working two ways
    keys = p1[co_points[0]:co_points[1]] + p2[co_points[0]:co_points[1]]
    values = p2[co_points[0]:co_points[1]] + p1[co_points[0]:co_points[1]]
    # segment dictionary
    segment = {keys[i]: values[i] for i in range(len(keys))}

    # empty offsprings
    o1 = [None] * len(p1)
    o2 = [None] * len(p2)

    # where pmx happens
    def pmx(o, p):
        for i, element in enumerate(p):
            # if element not in the segment, copy
            if element not in segment:
                o[i] = p[i]
            # if element in the segment, take the value of the key from
            # segment/dictionary
            else:
                o[i] = segment.get(element)
        return o

    # repeat the procedure for each offspring
    o1 = pmx(o1, p1)
    o2 = pmx(o2, p2)
    return o1, o2


def arithmetic_co(p1, p2):
    """Implementation of arithmetic crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)
    # Set a value for alpha between 0 and 1
    alpha = uniform(0, 1)

    # Take weighted sum of two parents, invert alpha for second offspring
    for i in range(len(p1)):
        offspring1[i] = p1[i] * alpha + (1 - alpha) * p2[i]
        offspring2[i] = p2[i] * alpha + (1 - alpha) * p1[i]

    return offspring1, offspring2

