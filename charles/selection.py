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
