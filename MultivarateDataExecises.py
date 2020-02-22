#Multivariate data exercises
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
pd.set_option("display.max_rows", 100)# Setting this to the max rows you expect eliminates the ellipsis
# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")
df
df.head() #first five rows ar displayed

### Keep only body measures columns, so only columns with "BMX" in the name

# get columns names
col_names = df.columns
col_names
# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
       'BMXWAIST']
	   
# Another way to get only column names that include 'BMX' is with list comprehension
# [keep x for x in list if condition met]
#List Comprehension [ expression for item in list if conditional ]
#[column for column in col_names if 'BMX' in column]
keep = [column for column in col_names if 'BMX' in column]
# use [] notation to keep columns
df_BMX = df[keep]
df_BMX.head()

# There are two methods for selecting by row and column.

# link for pandas cheat sheets
# df.loc[row labels or bool, col labels or bool]
# df.iloc[row int or bool, col int or bool]
# From pandas docs:
 # column indexing
# .loc is primarily label based, but may also be used with a boolean array.
# .iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.