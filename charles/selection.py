from random import uniform, sample, random
from operator import attrgetter

def tournament(population, size=15):

    """
    Tournament selection method
    Args:
        population: The population from which the selection method will act.
    Returns: an individual
    """

    # tourn_ind is a variable that stores the individuals selected to take part in the selection method
    tourn_ind = sample(population.individuals, size)

    if population.optim == "max":
        return max(tourn_ind, key=attrgetter("fitness"))

    elif population.optim == "min":
        return min(tourn_ind, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population: The population from which the selection method will act.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # total_fitness stores the sum of all fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        raise NotImplementedError ## VER

        # code adapted from https://rocreguant.com/roulette-wheel-selection-python/2019/
        # Computes the totality of the population fitness
        population_fitness = sum([individual.fitness for individual in population])

        # Computes for each individual the probability
        individual_probabilities = [individual.fitness / population_fitness for individual in population]

        # Making the probabilities for a minimization problem
        individual_probabilities = 1 - np.array(individual_probabilities)
        individual_probabilities = individual_probabilities / sum(individual_probabilities)

        #
        idx = list(range(len(population.individuals)))

        # test
        # check = sorted([(idx, p) for idx, p in enumerate(individual_probabilities)], key=lambda x: x[1], reverse=True)
        # Selects one individual based on the computed probabilities
        selected_idx = choice(idx, p=individual_probabilities)
        return population[selected_idx]

    else:
        raise Exception("No optimization specified (min or max).")

def rank(population): ##### VER
    """
    Rank selection implementation.

    Args:
        population: The population from which the selection method will act.

    Returns:
        Individual: selected individual.
    """
    # sorting individuals based on their fitness and if it is a maximization or minimization problem
    if population.optim == "max":
        population.individuals.sort(key=attrgetter("fitness"))
    elif population.optim == "min":
        population.individuals.sort(key=attrgetter("fitness"), reverse=True)
    else:
        raise Exception("No optimization specified (min or max).")

    #
    total = sum(range(population.size_pop + 1))

    spin = uniform(0, total)
    position = 0

    for count, individual in enumerate(population):
        position += count + 1
        if position > spin:
            return individual




