
from copy import deepcopy
from random import choice
import pandas as pd
import numpy as np
from random import sample
from initial_puzzle import easy
import math

print(math.isqrt(len([1,2,3])))
print(int(math.isqrt(len(easy)) + 0.5) ** 2 )

if int(math.isqrt(len([1,2,3])) + 0.5) ** 2 != len([1,2,3]):  # check if it is a square
    raise Exception(
        "The Sudoku's size must be the square of an integer number.")