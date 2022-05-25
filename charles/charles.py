from random import choice, random
import numpy as np
from copy import deepcopy
from operator import attrgetter
import pandas as pd
import time
import math

class Individual:
    def __init__(
                self,
                representation=None,
                initial_sudoku=None,
                valid_set=[i for i in range(1, 10)]):

        # index_missing will store the indexes that were not given in the start
        self.index_missing = [i for i in range(len(initial_sudoku)) if initial_sudoku[i] == 0]

        if initial_sudoku is None:
            raise Exception(
                "It is mandatory to provide an initial sudoku."
            )

        if len(initial_sudoku) != 81:
            raise Exception(
            "The Sudoku's size must be the square of an integer number."
        )

        if representation == None:

            #If a representation is not assigned, a possible solution is generated
            new_sudoku = deepcopy(initial_sudoku)

            # For each row
            for j in np.arange(0, 81, 9):
                number_missing = deepcopy(valid_set)

                for i in range(j, j+9):  # indexes for each 'row'
                    if i not in self.index_missing:# removing the numbers given from a list of possible numbers to fill
                        number_missing.remove(initial_sudoku[i])

                for i in range(j, j+9):
                    if i in self.index_missing:
                        new_sudoku[i] = choice(number_missing) #assigning a random number for each missing value(0)
                        number_missing.remove(new_sudoku[i])

            self.representation = deepcopy(new_sudoku)

        else: #if representation is defined by the user
            self.representation = representation

        self.fitness = self.get_fitness()

    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def get_neighbours(self, func, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"

class Population:
    def __init__(self, initial_sudoku, size_pop, optim, **kwargs):
        self.individuals = []
        self.size_pop = size_pop
        self.optim = optim
        self.initial_sudoku = initial_sudoku
        self.gen = 1

        # add individuals to the population
        for _ in range(size_pop):
            self.individuals.append(
                Individual(
                    initial_sudoku=initial_sudoku,
                    valid_set=kwargs["valid_set"]
                )
            )

    def evolve_run(self, runs, file_name, gens, select, crossover, mutate, co_p, mu_p, elitism):

        column_names = ['run', 'gen', 'bestfitness', 'mean_allfitness', 'time']
        df = pd.DataFrame(columns=column_names)

        best_found = 0
        ind_best = []

        # In every generation we start counting the time so that we know for how much time each generation run
        # We start a new population
        for gen in range(gens):
            new_pop = []
            start_time = time.time()

            # if there is elitism we choose the best individuals, according to the chosen fitness
            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size_pop:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                # Adding the new individual to the population
                new_pop.append(Individual(representation=offspring1, initial_sudoku=self.initial_sudoku))

                if len(new_pop) < self.size_pop:
                    new_pop.append(Individual(representation=offspring2, initial_sudoku=self.initial_sudoku))

            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))

                new_pop.pop(new_pop.index(least))

                # we append the best individual of the population to the new population
                new_pop.append(elite)

            self.individuals = new_pop
            total_time = time.time() - start_time

            # Creating a list with the fitnesses of every individual
            all_fitness = [ind.fitness for ind in self]

            # saving the best individual
            if best_found < max(self, key=attrgetter("fitness")).fitness:
                best_found = deepcopy(max(self, key=attrgetter("fitness")).fitness)
                ind_best = deepcopy(max(self, key=attrgetter("fitness")).representation)

            df2 = {'run': runs, 'gen': gen+1, 'bestfitness': max(self, key=attrgetter("fitness")).fitness, 'mean_allfitness':np.mean(all_fitness),'time':total_time}

            df = df.append(df2, ignore_index=True)

            print(f'Generation: {gen+1}')
            if self.optim == "max":
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            elif self.optim == "min":
                print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')

        print(max(self, key=attrgetter("fitness")).fitness)

        # saving the best solution in an array
        ind_best_array = np.asarray(max(self, key=attrgetter("fitness")).representation)
        reshaped_array = ind_best_array.reshape(9, 9)
        print(reshaped_array)

        df = df.append({'best_found': best_found}, ignore_index=True)
        df.to_csv(file_name, mode='a', index=False, header=False)

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"


