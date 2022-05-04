from random import uniform, sample, random
from operator import attrgetter

def tournament(population, size=10):

    """
        glfjgkç
    """

    tourn = sample(population.individuals, size)

    if population.optim == "max":
        return max(tourn, key=attrgetter("fitness"))

    elif population.optim == "min":
        return min(tourn, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # Sum total fitness
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

    else:
        raise Exception("No optimization specified (min or max).")

def rank(population):
    """
    Implementation of Rank selection.
    """
    # Rank individuals based on optim approach
    if population.optim == "max":
        population.individuals.sort(key=attrgetter("fitness"))
    elif population.optim == "min":
        population.individuals.sort(key=attrgetter("fitness"), reverse=True)
    else:
        raise Exception("No optimization specified (min or max).")

    # Sum all ranks
    total = sum(range(population.size + 1))
    # Get random position
    spin = uniform(0, total)
    position = 0
    # Iterate until spin is found
    for count, individual in enumerate(population):
        position += count + 1
        if position > spin:
            return individual




