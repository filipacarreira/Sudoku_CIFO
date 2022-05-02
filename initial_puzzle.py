
# Create the initial puzzles to be solved
import numpy as np
from copy import deepcopy

easy = [6,8,0,7,0,0,0,0,4,7,4,0,0,0,0,6,0,2,5,0,9,0,6,0,3,0,0,3,9,0,0,0,4,0,2,0,0,5,0,2,0,0,4,0,0,4,
        1,0,5,0,8,9,0,0,2,3,8,0,0,0,0,0,0,0,0,0,3,0,7,0,5,0,1,7,5,0,4,9,0,0,3]

medium = [6,0,0,0,5,0,8,0,1,5,0,0,9,0,0,6,7,2,0,0,0,0,1,3,0,4,0,0,0,0,8,0,2,0,5,7,2,0,8,0,0,5,0,9,0,7,0,0,0,9,0,0,8,4,3,7,4,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,4,0,0,0,0,0]

hard = [0,2,0,1,7,0,0,5,0,8,5,0,0,0,0,0,0,2,4,7,3,0,0,0,0,0,0,6,0,5,0,3,0,0,0,0,0,0,4,0,0,0,1,2,0,0,1,0,4,0,7,0,8,0,0,6,0,0,0,4,0,0,1,0,0,0,5,0,9,0,7,0,1,0,0,0,0,0,2,0,0]

print(len(hard))
print()
# Teste
fitness=0
for k in range(0,3): # first 3 blocks, second  blocks, third three blocks
        easy_partial=deepcopy(easy)
        easy_partial=easy_partial[k*27:k*27+27]
        print(easy_partial)
        for i in range(0,3): # for each block
                box = []
                for j in range(0,3): #for each line of the block
                        box.append(easy_partial[j*9 + i*3 : j*9 + i*3+3])
                print(box)
                box = [x for sublist in box for x in sublist]
                fitness+=len(set(box))
                print(fitness)


