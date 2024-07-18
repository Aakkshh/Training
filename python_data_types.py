# %% [markdown]
# DATA TYPES

# %%
# name = input("Enter your name") This is for name

# %% [markdown]
# List in built functions

# %%
list = [1, 2, 3]
list[1] = 3
list

# %% [markdown]
# Tuple

# %%
tuple = (1,2,3)
tuple[0] = 0

# %% [markdown]
# SET

# %%
set_var = {1,2,2}
set_var

# %% [markdown]
# Dictionary VS JSON
# 

# %%
dict = {"A": 1, "B":2}
dict

# %% [markdown]
# OPERATORS

# %% [markdown]
# ENUM

# %%
from enum import Enum

class State(Enum):
    Active = 1
    InActive = 0
    
print(State.Active.value)

# %% [markdown]
# Functions

# %% [markdown]
# isinstance, type

# %%
def func():
    return "Hello"
def add(x, y):
    
    return x + y
func()
add(1,2)

# %%



