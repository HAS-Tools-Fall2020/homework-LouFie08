# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd

# %%

x1 = np.arange(1,11,1)
print(x1)
x2 = 1.3
dx1=x1//x2
answer=np.floor_divide(x1,x2)
print(answer)
print(dx1)
x1_mx = max(dx1)

# x1 = np.divide(np.arange(0,11,1),1.3).astype(int)

# l=np.max()
# %%
x1 = [0,4,37,17]
x2 = [1.2,3,4.6,7]

answer = np.round(np.divide(x1,x2),decimals=2)

# %% 
# np.random, np.round,np.mean,np.std

# %% PANDAS!!!!!

data = pd.Series([0.1,50,47,1.367],index=['a','b','c','d'])
data.values
print(data)
# %%

rng = np.random.RandomState(42) # This holds rand no constant
dataframe = pd.DataFrame(rng.randint(0,10,(3,3)),columns=['b','a','c'],
            index=['row1','row2','row3'])
dataframe.b
dataframe.values
print(dataframe)
m = np.mean(dataframe.b)
n = np.mean(dataframe['b'])
dataframe.columns
dataframe['b']
# let you find rows by their names
dataframe.loc['row1','a']

# let you find rows by their numbers
dataframe.iloc[0,1]
# %%
