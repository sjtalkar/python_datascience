from  pandas import DataFrame
import numpy as np

#Creating DataFrame from a Dictionary
firstProductSet = {'Product1': ['Computer','Phone','Printer','Desk'],
                   'Price1': [1200,800,200,350]
                   }
df1 = DataFrame(firstProductSet,columns= ['Product1', 'Price1'])
#df1

secondProductSet = {'Product2': ['Computer','Phone','Printer','Desk'],
                    'Price2': [900,800,300,350]
                    }
df2 = DataFrame(secondProductSet,columns= ['Product2', 'Price2'])

#df2

df1['Price2'] = df2['Price2'] #add the Price2 column from df2 to df1

df1['pricesMatch?'] = np.where(df1['Price1'] == df2['Price2'], 'True', 'False')  #create new column in df1 to check if prices match
df1['priceDiff?'] = np.where(df1['Price1'] == df2['Price2'], 0, df1['Price1'] - df2['Price2']) #create new column in df1 for price diff 
print (df1)

   # Product1  Price1  Price2 pricesMatch?  priceDiff?
# 0  Computer    1200     900        False         300
# 1     Phone     800     800         True           0
# 2   Printer     200     300        False        -100
# 3      Desk     350     350         True           0

import pandas as pa
import seaborn as sns # For plotting
import matplotlib.pyplot as plt
tips_data = pa.read_csv("C:\\PYTHONDATASCIENCE\\tips.csv")
tips_data
tips_data.head()

#Find the unique values of a column
tips_data.time.value_counts()

#Check to see if we have any NULLS in column "time"
#pa.isnull(tips_data.time).sum()

#Decoding an  code or a value  into user friedly literal
tips_data["time"] = tips_data.time.replace({"Dinner": "Dinner After 8 PM", "Lunch": "Lunch After 11 AM"})
tips_data.time.value_counts()


#Another example RIAGENDRx is a column in the dataframe da
#da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})


#  
a["DMDEDUC2x"] = da.DMDEDUC2x.fillna("Missing")
x = da.DMDEDUC2x.value_counts()
x / x.sum()

#Ignore nulls before getting mean median
da.BMXWT.dropna().describe()