from random import choice, random
import numpy as np
from copy import deepcopy


class Individual:
    def __init__(
        self,
        representation=None,
        initial_sudoku=None,
        valid_set=[i for i in range(1, 10)]):

        self.fitness = self.get_fitness()
        self.index_missing = [i for i in range(len(initial_sudoku)) if initial_sudoku[i] == 0]

        if initial_sudoku is None:
            raise Exception(
                "It is mandatory to provide an initial sudoku."
            )

        if np.sqrt(len(initial_sudoku)).is_integer():# check if it ia a square
            raise Exception(
                "The Sudoku's size must be the square of an integer number."
            )

        if representation == None:# If a representation is not assigned, a possible solution is generated
            new_sudoku = initial_sudoku.deepcopy()
            # For each row
            for j in np.arange(0, 81, 9):
                number_missing = valid_set.deepcopy()
                for i in range(j, j+9):  # indexes for each 'row'
                    if i not in self.index_missing:# removing the numbers given from a list of possible numbers to fill
                        number_missing.remove(initial_sudoku[i])
                for i in range(j, j+9):
                    if i in self.index_missing:
                        new_sudoku[i] = choice(number_missing) #assigning a random number for each missing value (0)
                        number_missing.remove(new_sudoku[i])
            self.representation = new_sudoku.deepcopy() ###### VER########

        else:# if representation is defined by the user
            self.representation = representation

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
    def __init__(self, initial_sudoku, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.initial_sudoku = initial_sudoku
        self.gen = 1

        for _ in range(size):
            self.individuals.append(
                Individual(
                    grid_initial=initial_sudoku,
                    size=kwargs["sol_size"], #### ver ####
                    valid_set=kwargs["valid_set"], #### ver ####
                )
            )

