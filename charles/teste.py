
from copy import deepcopy
from random import choice
import pandas as pd
import numpy as np
from random import sample
from initial_puzzle import easy
import math
teste=[8,4,6,9,3,7,1,5,2,3,1,9,6,2,5,8,4,7,7,5,2,1,8,4,9,6,3,2,8,5,7,1,3,6,9,4,4,6,3,8,5,9,2,7,1,9,7,1,2,4,6,3,8,5,1,2,7,5,9,8,4,3,6,6,3,8,4,7,1,5,2,9,5,9,4,3,6,2,7,1,8]
print(len(teste))
fitness_value = 0
# get rows' fitness
for row in np.arange(0, 81, 9):
    fitness_value += len(set(teste[row:row+9]))

# get columns' fitness
for columns in range(0, 9):
    column_evaluate = []
    for elem in [index + columns for index in np.arange(0, 81, 9)]:
        column_evaluate.append(teste[elem])
    fitness_value += len(set(column_evaluate))

# get boxs' fitness
# creating these variables to make the code susceptible to different Sudoku sizes

base = 3
len_box = 9
len_line_box = 27

for k in range(0, base):
        #first 3 blocks, second  blocks, third three blocks
        box_partial = deepcopy(teste)
        box_partial = box_partial[k*len_line_box : k*len_line_box+len_line_box]
        for i in range(0, base):#for each block
                box = []
                for j in range(0, base): #for each line of the block
                        box.append(box_partial[j*len_box + i*base : j*len_box + i*base+base])
                box = [x for sublist in box for x in sublist]
                fitness_value += len(set(box))

print(fitness_value)