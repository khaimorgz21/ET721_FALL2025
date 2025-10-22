"""
Makhai Morgan
Oct 22, 2025
lab 11, APIs
"""
import pandas as pd

# --------------
# 1. example dataframe
#----------------
dict_ = {'a':[11,21,31],  'b':[12,22,32]}

# create a dataframwe for dict_
df = pd.DataFrame(dict_)

# display the first few rows of the dataframe
print(df.head())