from random import sample, random, randint
from copy import deepcopy

def mutation_sample(indiv, number_mut=3):
    """
    Mutation Sample for a GA individual - mutation created specifically for the Sudoku problem
    Choosing a number of elements to mutate in the individual and change them with a random choice of numbers
    (taking into account the possible representation of each individual)

    Args:
        individual (Individual): A GA individual from charles.py
        number_mut : number of elements of the individual to mutate

    Returns:
        Individual: Mutated Individual
    """

    # saving the indexes to mutate, based in the provided number of elements to mutate
    # only considering the indexes of elements that are not in the original puzzle
    indexes_mut = sample(indiv.index_missing, k=number_mut)[0] # used sample instead of choices because of the non 'replacement' factor
                                                               # we don't want to mutate the same element twice

    # For every index, we create a random number between 1 and 9 to put in that index
    for i in indexes_mut:
        indiv[i] = sample([i for i in range(1, 10)], k=1)[0]

    return indiv

def mutation_prob(indiv, prob):
    """
    Mutation Probability for a GA individual - mutation created specifically for the Sudoku problem
    This mutation occurs in each index of the individual with a provided probability of being replaced with
    a random choice of the valid set of values of the individual
    (the valid set is chosen due to the representation of the individual - valid_set)

    Args:
        individual (Individual): A GA individual from charles.py
        prob : probability of applying the mutation

    Returns:
        Individual: Mutated Individual
    """
    # Considering only the indexes of elements that are not in the initial puzzle
    for i in indiv.index_missing:
        # we choose a random number between 1 and 9 to give to each element of the individual
        if random() < prob:
            indiv[i] = sample(indiv.valid_set, k=1)
    return indiv

def mutation_swap (indiv):

    """
    Mutation Swap for a GA individual - mutation created specifically for the Sudoku problem
    Randomly chose if the crossover is applied to columns, rows or boxes
    After choosing the "variable" to use, we choose 2 elements of the variable to swap between them

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """

    # Choosing which "variable" to swap
    # 0 = Swapping rows
    # 1 = Swapping columns
    # 3 = Swapping boxes
    random_decision = sample(range(0, 3), k=1)[0]

    if random_decision == 0: #do mutation by rows

        # choosing a random row and saving the index of its first element
        ind_chosen = sample(range(0, 9), k=1)[0] * 9
        # getting the indexes of the elements we can change (the ones that were not in the initial puzzle)
        missing_row = list(set(indiv.index_missing).intersection(set(range(ind_chosen, ind_chosen+9))))

        # choosing two elements in the row to swap
        choose_2 = sample(missing_row, k=2)
        indiv_orig = deepcopy(indiv)

        # swapping the elements
        indiv[choose_2[0]] = indiv[choose_2[1]]
        indiv[choose_2[1]] = indiv_orig[choose_2[0]]

    elif random_decision == 1: # do mutation by columns

        # choosing a random column
        ind_chosen = sample(range(0, 9), k=1)[0]

        # saving the indexes of the selected column
        ind_column = [ind_chosen+(i*9) for i in range(0, 9)]

        # getting the indexes of the elements we can change (the ones that were not in the initial puzzle)
        missing_column = list(set(indiv.index_missing).intersection(set(ind_column)))

        # choosing two elements in the column to swap
        choose_2 = sample(missing_column, k=2)

        # swapping the elements
        indiv_orig = deepcopy(indiv)
        indiv[choose_2[0]] = indiv[choose_2[1]]
        indiv[choose_2[1]] = indiv_orig[choose_2[0]]

    elif random_decision == 2: # do mutation by boxes
        # Choose a random block
        # A block is a set of 3 boxes 3*3 (so basically indicates the 3 boxes in the firsts rows of the sudoku)
        block_chosen = sample(range(0, 3), k=1)[0]

        # From the block chosen, choose a random box
        box_chosen = sample(range(0, 3), k=1)[0]

        # saving the first index of the box chosen
        ind_initial = block_chosen*27 + box_chosen*3
        missing_box = []

        for k in range(0, 3): # 3 lines
            # Saving the indexes inside the boxes
            ind_box = [ind_initial+i + k*9 for i in range(0, 3)]

            # Saving the indexes that can be changed (that weren't present in the initial puzzle)
            missing_box = missing_box + list(set(indiv.index_missing).intersection(set(ind_box)))

        # Choosing 2 elements in the box to swap
        choose_2 = sample(missing_box, k=2)

        indiv_orig = deepcopy(indiv)

        # Swapping the elements
        indiv[choose_2[0]] = indiv[choose_2[1]]
        indiv[choose_2[1]] = indiv_orig[choose_2[0]]


    return indiv


def mutation_swap_all(indiv):
    """
    Mutation Swap All for a GA individual - mutation created specifically for the Sudoku problem
    Similar to Mutation Swap above defined
    The difference is that instead of choosing 2 elements to swap, we swap the whole individual
    The indexes that were already filled in the initial puzzle are taken into account, so we only swap the indexes missing

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """

    # Choosing which "variable" to swap
    # 0 = Swapping rows
    # 1 = Swapping columns
    # 3 = Swapping boxes
    random_decision = sample(range(0, 3), k=1)[0]

    if random_decision == 0:  # do mutation by rows
        # Choosing the row to swap and saving the first index
        ind_chosen = sample(range(0, 9), k=1)[0] * 9
        # Saving the indexes of the row that can be changed
        missing_row = list(set(indiv.index_missing).intersection(set(range(ind_chosen, ind_chosen + 9))))

        # Shuffling the indexes of the row
        missing_sampled = sample(missing_row, len(missing_row))

        indiv_orig = deepcopy(indiv)

        # For every element in the indexes that can be changed, we give the value of the correspondent index in the shuffled list
        for i in range(len(missing_row)):

            indiv[missing_row[i]] = indiv_orig[missing_sampled[i]]

    elif random_decision == 1:  # do mutation by columns

        # Choosing the column to swap and saving the first index
        ind_chosen = sample(range(0, 9), k=1)[0]

        # Saving the indexes of the column and the ones that can be changed
        ind_column = [ind_chosen + (i * 9) for i in range(0, 9)]
        missing_column = list(set(indiv.index_missing).intersection(set(ind_column)))

        # Shuffling the indexes of the column
        missing_sampled = sample(missing_column, len(missing_column))

        indiv_orig = deepcopy(indiv)

        # For every element in the indexes that can be changed, we give the value of the correspondent index in the shuffled list
        for i in range(len(missing_column)):
            indiv[missing_column[i]] = indiv_orig[missing_sampled[i]]

    elif random_decision == 2: # do mutation by boxes

        # Choosing a random block
        # A block is a set of 3 boxes 3*3 (so basically indicates the 3 boxes in the firsts rows of the sudoku)
        block_chosen = sample(range(0, 3), k=1)[0]

        # Inside the block, choose a random box to swap
        box_chosen = sample(range(0, 3), k=1)[0]

        # Save the initial index of the box
        ind_initial = block_chosen * 27 + box_chosen * 3
        missing_box=[]

        for k in range(0, 3):  # 3 lines
            ind_box = []
            # Saving the indexes of the box
            ind_box = [ind_initial + i + k * 9 for i in range(0, 3)]
            # Saving the indexes of the box that can be changed (because they weren't in the initial puzzle)
            missing_box = missing_box + list(set(indiv.index_missing).intersection(set(ind_box)))

        # Shuffling the elements of the box
        missing_sampled = sample(missing_box, len(missing_box))

        indiv_orig = deepcopy(indiv)

        # For every element in the indexes that can be changed, we give the value of the correspondent index in the shuffled list
        for i in range(len(missing_box)):
            indiv[missing_box[i]] = indiv_orig[missing_sampled[i]]

    return indiv

## NOT USED - The methods under did not make sense in the context of our problem
#             since we have to take into account the numbers present in the initial puzzle

def binary_mutation(individual):
    """Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    # Choosing a random index to do the mutation
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary.")

    return individual


def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    mut_points = sample(range(len(individual)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    individual[mut_points[0]:mut_points[1]] = individual[mut_points[0]:mut_points[1]][::-1]

    return individual


