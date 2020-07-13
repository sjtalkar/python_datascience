def convert_housing_data_to_quarters():
    """Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    """

    return "ANSWER"


# A quarter is a specific three month period, Q1 is January through March,
# Q2 is April through June, Q3 is July through September, Q4 is October through December.

len(zillow_allhomes_df)
zillow_allhomes_df.columns
# Index(['RegionID', 'RegionName', 'State', 'Metro', 'CountyName', 'SizeRank', '2016-01', '2016-02', '2016-03', '2016-04',
temp_zillow = zillow_allhomes_df[zillow_allhomes_df["State"] == "WA"]

# print((2016-2000 + 1 ) * 4)

# separate time columns and convert their names to datetime
temp_zillow = temp_zillow[temp_zillow.columns[6:]].rename(columns=pd.to_datetime)

column_we_need = temp_zillow.columns
column_we_need = column_we_need[
    (column_we_need > "1999-12-31") & (column_we_need < "2016-09-01")
]
len(column_we_need) / 3

temp_zillow[column_we_need]


temp_zillow = temp_zillow[column_we_need].resample("QS", axis=1).mean()
# quarterly_mean


month_names = temp_zillow.columns
month_names = pd.PeriodIndex(month_names, freq="Q")

temp_zillow.columns = month_names

# zillow_allhomes_df[zillow_allhomes_df.columns[:6]]
temp_zillow[temp_zillow.columns[:6]]


# print (tabulate(mdf[mdf.columns[0:9]].iloc[
#        23:29], headers='keys', tablefmt='orgtbl'))

