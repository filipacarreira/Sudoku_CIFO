
from copy import deepcopy
from random import choice
import pandas as pd
var=5
df = pd.DataFrame(columns=['hello', 'adeus'])
df=df.append({'hello':var},ignore_index=True)
print(df)

