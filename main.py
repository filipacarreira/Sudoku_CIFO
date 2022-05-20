from copy import deepcopy
from charles.charles import Population, Individual
from initial_puzzle import easy, medium, hard
from charles.selection import fps, tournament, rank
from charles.crossover import in_common_co, in_common_prob_co, swap_elements_co
from charles.mutation import mutation_swap, mutation_swap_all
import numpy as np
from operator import attrgetter

def get_fitness(self):
    """ This function computes fitness scores of each individual (a possible solution).
       Since it considers the number of unique digits in each row, column and box, the maximum fitness is 243 (81*3)

       Returns:
           fitness_value (int): the fitness for a sudoku solution
    """

    # initializing and declaring a variable that will store the fitness value of a solution
    fitness_value = 0

    # get rows' fitness
    for row in np.arange(0, 81, 9):
        fitness_value += len(set(self.representation[row:row+9]))

    # get columns' fitness
    for columns in range(0, 9):
        column_evaluate = []
        for elem in [index + columns for index in np.arange(0, 81, 9)]:
            column_evaluate.append(self.representation[elem])
        fitness_value += len(set(column_evaluate))

    # get boxs' fitness

    base = 3
    len_box = 9
    len_line_box = 27

    for k in range(0, base):
            #first 3 blocks, second  blocks, third three blocks
            box_partial = deepcopy(self.representation)
            box_partial = box_partial[k*len_line_box : k*len_line_box+len_line_box]
            for i in range(0, base):#for each block
                    box = []
                    for j in range(0, base): #for each line of the block
                            box.append(box_partial[j*len_box + i*base : j*len_box + i*base+base])
                    box = [x for sublist in box for x in sublist]
                    fitness_value += len(set(box))

    return fitness_value

# the neighborhood does not apply for this specific problem
def get_neighbours (self):
    pass

# monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

#pop_easy = Population(size_pop=5000,file_name='test', optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])

#pop_easy.evolve_run(run=2, gens=6, file_name='test.csv', select=tournament, crossover=swap_lines, mutate=mutation_swap, co_p = 0.95, mu_p = 0.01, elitism=True)

#fitness = 224, gens=100, select=rank, crossover=uniform_co_alt, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True

# =============================  Tries ==============================

#fitness 239, tournament=5
#pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#pop_easy.evolve_run(run=3, gens=10, file_name='performance/test3.csv', select=tournament, crossover=swap_lines, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


#tournament=10
#pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])


# tournament 10 pop 5000
#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=30, file_name='performance/easy_tour_swapco_mut_swap_all.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap_all, co_p = 0.90, mu_p = 0.1, elitism=True)


# tournament 10 pop size 5000
#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/easy_tour10_swapco_mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


# tournament 20 pop size 5000
#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=30, file_name='performance/easy_tour20_swapco_mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


#run = 10 BEST
#for i in range(run):
#   pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/easy_tour5_swapco_mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/easy_tour5_co_incommon_mut_swap.csv', select=tournament, crossover=in_common_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/easy_tour5_swapco_mut_swapall.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/easy_tour10_swapco_mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/easy_tour5_95swapco_5mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.95, mu_p = 0.05, elitism=True)


#run = 10
#for i in range(run):
#    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=medium, valid_set=[i for i in range(1, 10)])
#    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/medium_tour5_swapco_mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)


run = 10
for i in range(run):
    pop_easy = Population(size_pop=5000, optim="max", initial_sudoku=hard, valid_set=[i for i in range(1, 10)])
    pop_easy.evolve_run(runs=i+1, gens=40, file_name='performance/hard_tour5_swapco_mut_swap.csv', select=tournament, crossover=swap_elements_co, mutate=mutation_swap, co_p = 0.90, mu_p = 0.1, elitism=True)
