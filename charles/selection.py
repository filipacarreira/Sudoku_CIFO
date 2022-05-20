from random import uniform, sample, random, choice
from operator import attrgetter

def tournament(population, size=5):

    """
    Tournament selection method
    Args:
        population: The population from which the selection method will act.
    Returns: an individual
    """

    #tourn_ind is a variable that stores the individuals selected to take part in the selection method

    tourn_ind = sample(population.individuals, size)
    #tourn_ind = [choice(population.individuals) for i in range(size)]

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

        # Sum total fitnesses
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = random()
        position = 0

        # Find individual in the position of the spin
        for individual in population:

            # (1 - individual.fitness / total_fitness) to ensure the higher the fitness,
                # the lower the probability for that individual should be.
            position += (1 - individual.fitness / total_fitness)

            if position > spin:
                return individual
    else:
        raise Exception("No optimization specified (min or max).")

def rank(population):
    """
    Rank selection

    Args:
        population: The population from which the selection method will act.

    Returns:
        Individual: selected individual.
    """
    # Sort individuals according to the optimization choice
    if population.optim == "max":
        population.individuals.sort(key=attrgetter("fitness"))
    elif population.optim == "min":
        population.individuals.sort(key=attrgetter("fitness"), reverse=True)
    else:
        raise Exception("No optimization specified (min or max).")

    # Sum all ranks
    total = sum(range(population.size + 1))
    # Get a random spin
    spin = uniform(0, total)
    position = 0

    #  Find individual in the position of the spin
    for count, individual in enumerate(population):
        position += count + 1
        if position > spin:
            return individual




