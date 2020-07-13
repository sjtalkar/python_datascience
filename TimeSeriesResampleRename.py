zillow_allhomes_df = pd.read_csv("City_Zhvi_AllHomes.csv")
zillow_allhomes_df.head()


zillow_allhomes_df.tail()
# Index(['RegionID', 'RegionName', 'State', 'Metro', 'CountyName', 'SizeRank', '2016-01', '2016-02', '2016-03', '2016-04',
temp_zillow = zillow_allhomes_df.copy()
#  convert column  names to datetime
temp_zillow.set_index(["State", "RegionName"], inplace=True)

temp_zillow = temp_zillow[temp_zillow.columns[6:]].rename(columns=pd.to_datetime)
# print(temp_zillow.shape)

columns_we_need = temp_zillow.columns
columns_we_need = columns_we_need[
    (columns_we_need > "1999-12-31") & (columns_we_need < "2016-09-01")
]

temp_zillow = temp_zillow[columns_we_need].resample("QS", axis=1).mean()


# Convert dates to Quarter periods
month_names = temp_zillow.columns
month_names = pd.PeriodIndex(month_names, freq="Q")

# Assign Quater names as column names
temp_zillow.columns = month_names
zillow_allhomes_df = temp_zillow
zillow_allhomes_df.iloc[18]
zillow_allhomes_df.loc[("WA", "Seattle")]

