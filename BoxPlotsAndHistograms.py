# We first need to import the packages that we will be using

#USe the below in the course Jupyter notebook to export the tips dataframe
tips_data.to_csv(r'C:\PYTHONDATASCIENCE\tips.csv')

# Open File in the note book and you will find this file 
#C:\PYTHONDATASCIENCE\tips.csv


#pip install seaborn
#pip install -U matplotlib

import pandas as pa
import seaborn as sns # For plotting

#IMPORTANT USE matplotlib.pyplot NOT just matplotlib as it will cause show error
import matplotlib.pyplot as plt

# Load in the data set This did not work with local csv and so used read_csv from pandas
#tips_data = sns.load_dataset("tips")

type(tips_data)
#pandas.core.frame.DataFrame



tips_data = pa.read_csv("C:\\PYTHONDATASCIENCE\\tips.csv")
tips_data
tips_data.head()
type(tips_data)
#pandas.core.frame.DataFrame


tips_data.columns
#Index([u'total_bill', u'tip', u'sex', u'smoker', u'day', u'time', u'size'], dtype='object')

#tips_data.loc[tips_data.index.map(crit)]

# Print out the first few rows of the data
tips_data.head()

# Print out the summary statistics for the quantitative variables
tips_data.describe()

# id	total_bill	tip	size
# count	244.000000	244.000000	244.000000	244.000000
# mean	121.500000	19.785943	2.998279	2.569672
# std	70.580923	8.902412	1.383638	0.951100
# min	0.000000	3.070000	1.000000	1.000000
# 25%	60.750000	13.347500	2.000000	2.000000
# 50%	121.500000	17.795000	2.900000	2.000000
# 75%	182.250000	24.127500	3.562500	3.000000
# max	243.000000	50.810000	10.000000	6.000000

#tips_data.head()
sns.distplot(tips_data["total_bill"], kde = False).set_title("Histogram of Total Bill")
plt.show()

tips_data.describe()
tips_data.head()
sns.distplot(tips_data["total_bill"], kde = False).set_title("Histogram of Total Bill")
plt.show()

Plot a histogram of the Tips only
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Total Tip")
plt.show()


sns.boxplot(tips_data["total_bill"]).set_title("Box plot of the Total Bill")
plt.show()


sns.boxplot(tips_data["total_bill"]).set_title("Box plot of the Total Bill")
plt.show()

# Create a boxplot of the tips and total bill amounts - do not do it like this
sns.boxplot(tips_data["total_bill"])
sns.boxplot(tips_data["tip"]).set_title("Box plot of the Total Bill and Tips")
plt.show()


#Qualitative data
sns.boxplot(x = tips_data["tip"], y = tips_data["smoker"])
plt.show()
sns.boxplot(x = tips_data["tip"], y = tips_data["time"])

# Create a boxplot and histogram of the tips grouped by time of day
sns.boxplot(x = tips_data["tip"], y = tips_data["time"])

g = sns.FacetGrid(tips_data, row = "time")
g = g.map(plt.hist, "tip")
plt.show()

sns.boxplot(x = tips_data["tip"], y = tips_data["day"])

g = sns.FacetGrid(tips_data, row = "day")
g = g.map(plt.hist, "tip")
plt.show()



# Frequency tables
# The value_counts method can be used to determine the number of times that each distinct value of a variable occurs in a data set. In statistical terms, this is the "frequency distribution" of the variable. 

da.BMXWT.dropna().describe()