
# Question 1
# Relabel the marital status variable DMDMARTL to have brief but informative character labels. 
# Then construct a frequency table of these values for all people, then for women only, and for men only.
# Then construct these three frequency tables using only people whose age is between 30 and 40.

 
#From website https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDMARTL 
# 1	Married	2886	2886	
# 2	Widowed	421	3307	
# 3	Divorced	614	3921	
# 4	Separated	192	4113	
# 5	Never married	1048	5161	
# 6	Living with partner	555	5716	
# 77	Refused	2	5718	
# 99	Don't Know	1	5719	
# .	Missing	4252	9971	


#Relabel the marital status variable DMDMARTL to have brief but informative character labels.


#Relabel the marital status variable DMDMARTL to have brief but informative character labels.

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")


da.DMDMARTL.unique()
da["DMDMARTLCONV"] = da.DMDMARTL.replace({1: "Married",2:"Widowed", 3: "Divorced", 4: "Separated", 5: "Never married", 
                                            6:"Living with partner", 77:"Refused", 99:"Don't know"})

da.DMDMARTLCONV.unique()

print(da.RIAGENDR.unique())
#1 Male
#2 Female

#Then construct a frequency table of these values for all people
da.DMDMARTLCONV.value_counts()

da["RIAGENDRCONV"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da.RIAGENDRCONV.unique()



#Then construct a frequency table of these values : then for women only
#da.columns
da["gender"] = pd.cut(da.RIAGENDR, [1, 2]) # Create gender strata based on these cut points
da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])


da.groupby("gender")["DMDMARTLCONV"].value_counts()

#Then construct a frequency table of these values  for men only.

#Then construct a frequency table of these values for all people
#da.gender


# RIAGENDR  DMDMARTLCONV       
# 1         Married                1477
          # Never married           484
          # Living with partner     265
          # Divorced                229
          # Widowed                 100
          # Separated                68
          # Refused                   1
# 2         Married                1303
          # Never married           520
          # Divorced                350
          # Widowed                 296
          # Living with partner     262
          # Separated               118
          # Refused                   1
# Name: DMDMARTLCONV, dtype: int64


# dx = da.loc[~da.DMDEDUC2x.isin(["Don't know", "Missing"]), :]  # Eliminate rare/missing values
# dx = dx.groupby(["agegrp", "RIAGENDRx"])["DMDEDUC2x"]
# dx = dx.value_counts()
# dx = dx.unstack() # Restructure the results from 'long' to 'wide'
# dx = dx.apply(laa x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
# print(dx.to_string(float_format="%.3f"))  # Limit display to 3 decimal place



da.DMDMARTL.unique()
da["DMDMARTLCONV"] = da.DMDMARTL.replace({1: "Married",2:"Widowed", 3: "Divorced", 4: "Separated", 5: "Never married", 
                                            6:"Living with partner", 77:"Refused", 99:"Don't know"})

da.DMDMARTLCONV.unique()

print(da.RIAGENDR.unique())

#Then construct a frequency table of these values for all people
da.DMDMARTLCONV.value_counts()

da["RIAGENDRCONV"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da.RIAGENDRCONV.unique()



#Then construct a frequency table of these values : then for women only
#da.columns
da["gender"] = pd.cut(da.RIAGENDR, [1, 2]) # Create gender strata based on these cut points
da.groupby("gender")["DMDMARTLCONV"].value_counts()

#Then construct a frequency table of these values  for men only.

#Then construct a frequency table of these values for all people
da.DMDMARTLCONV.value_counts()

da["gender"] = pd.cut(da.RIAGENDR, [1, 2]) # Create gender strata based on these cut points
da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])

#da.gender
da.groupby(da.RIAGENDR)["DMDMARTLCONV"].value_counts()

#STATEGY 2 Separate the frame into Women and Men
da.count()
mdx = da.loc[da.RIAGENDR.isin([1]), :]  # Eliminate rare/missing values
wdx = da.loc[da.RIAGENDR.isin([2]), :]  # Eliminate rare/missing values
wdx["DMDMARTLCONV"].value_counts()
mdx["DMDMARTLCONV"].value_counts()


da.groupby([da.RIAGENDR, "agegrp"])["DMDMARTLCONV"].value_counts()


## Question 2

#Restricting to the female population, stratify the subjects into age bands no wider than ten years, and construct the distribution of marital status within each age band.  Within each age band, present the distribution in terms of proportions that must sum to 1.
# insert your code here#Frequency count for only women
wdx["DMDMARTLCONV"].value_counts()
#Splitting by age band
wdx.groupby(["agegrp"])["DMDMARTLCONV"].value_counts()


# insert your code here#Frequency count for only women
wdx["DMDMARTLCONV"].value_counts()

wdx = wdx.groupby(["agegrp"])["DMDMARTLCONV"]
wdx = wdx.value_counts()
wdx = wdx.unstack() # Restructure the results from 'long' to 'wide'
wdx = wdx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
print(wdx.to_string(float_format="%.3f")) 


# insert your code here#Frequency count for only men
mdx["DMDMARTLCONV"].value_counts()

mdx = mdx.groupby(["agegrp"])["DMDMARTLCONV"]
mdx = mdx.value_counts()
mdx = mdx.unstack() # Restructure the results from 'long' to 'wide'
mdx = mdx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
print(mdx.to_string(float_format="%.3f")) 



#Question 3
#Construct a histogram of the distribution of heights using the BMXHT variable in the NHANES sample.
sns.distplot(da.BMXHT.dropna())

mdx = da.loc[da.RIAGENDR.isin([1]), :]  
wdx = da.loc[da.RIAGENDR.isin([2]), :]

sns.distplot(mdx.BMXHT.dropna())

sns.distplot(wdx.BMXHT.dropna())


#BOXPLOTS OF MEN AND WONEN AND HEIGHTS
da["RIAGENDRCONV"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da.columns

sns.boxplot(x="RIAGENDRCONV", y="BMXHT", hue="RIAGENDRCONV", data=da)



## Question 5

#Construct a frequency table of household sizes for people within each educational attainment category (the relevant variable is 
#[DMDEDUC2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2)).  Convert the frequencies to proportions.
da["DMDEDUC2CONV"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
                                       7: "Refused", 9: "Don't know"})
da["DMDEDUC2CONV"].value_counts()
​
# Some college/AA    1621
# College            1366
# HS/GED             1186
# <9                  655
# 9-11                643
# Don't know            3
# Name: DMDEDUC2CONV, dtype: int64





#Q5b. Restrict the sample to people between 30 and 40 years of age. 
#Then calculate the median household size for women and men within each level of educational attainment.
## LIMIT DATA TO THOSE WIth age between 30 and 40

da.count()

restda = da.loc[(da['RIDAGEYR'] >= 30) & (da['RIDAGEYR'] <= 40)]
restda.RIDAGEYR

da.count()

restda = da.loc[(da['RIDAGEYR'] >= 30) & (da['RIDAGEYR'] <= 40)]
restda.groupby([da.RIAGENDR])["DMDHHSIZ"].describe()

	# count	mean	std	min	25%	50%	75%	max
# RIAGENDR								
# 1	494.0	3.925101	1.709198	1.0	3.0	4.0	5.0	7.0
# 2	532.0	4.148496	1.597590	1.0	3.0	4.0	5.0	7.0

# This will give median in a boxplot
restda = da.loc[(da['RIDAGEYR'] >= 30) & (da['RIDAGEYR'] <= 40), :]

restda.groupby([da.RIAGENDR])["DMDHHSIZ"].describe()
restda.groupby([da.RIAGENDR])["DMDHHSIZ"].median()
sns.boxplot(x="RIAGENDRCONV", y="DMDHHSIZ", hue="RIAGENDRCONV", data=restda)