from random import sample, random

def mutation_sample(indiv,number_mut):
    """
    """

    indexes_mut = sample(indiv.index_missing, k=number_mut) # used sample instead of choices because of the non 'replacement' factor

    for i in indexes_mut:
        indiv[i] = sample(indiv.valid_set, k=1)

    return indiv

def mutation_prob(indiv, prob):
    """
    """

    for i in indiv.index_missing:
        if random() < prob:
            indiv[i] = sample(indiv.valid_set, k=1)

    return indiv