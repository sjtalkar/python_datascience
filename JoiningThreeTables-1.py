def answer_one():
    
    energy = pd.read_excel('Energy Indicators.xls', header = 15, skipfooter= 38)
    energy.rename(columns = {
        energy.columns[2]: 'Country',
        energy.columns[3]: 'Energy Supply',
        energy.columns[4]: 'Energy Supply per Capita',
        energy.columns[5]: '% Renewable'},
        inplace = True)



    energy.drop(energy.index[0], inplace=True)


    energy.drop(energy.iloc[:, 0:2], inplace = True, axis = 1) 


    # 7)For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
    energy = energy.applymap(lambda x: np.nan if str(x) == '...' else x)



    #8) There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
    energy['Country'] = energy['Country'].str.split('[\d\(]') # split the index by '('

    energy['Country'] = energy['Country'].str[0]
    energy['Country'] =  energy['Country'].str.strip()


    energy.replace(value='South Korea' , to_replace= 'Republic of Korea', inplace=True)
    energy.replace(value= 'United States', to_replace= 'United States of America', inplace=True)
    energy.replace(value= 'United Kingdom', to_replace='United Kingdom of Great Britain and Northern Ireland', inplace=True)
    energy.replace(value= 'Hong Kong', to_replace = 'China, Hong Kong Special Administrative Region', inplace=True)    

    energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'] / (10 ** 6)

    GDP = pd.read_csv('world_bank.csv', header=4)
    pd.set_option('display.max_rows', 300)

    
    GDP.replace(value= 'South Korea', to_replace= 'Korea, Rep.', inplace=True)
    GDP.replace(value= 'Iran', to_replace= 'Iran, Islamic Rep.', inplace=True)
    GDP.replace(value= 'Hong Kong', to_replace='Hong Kong SAR, China, inplace=True)
    
    
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    
    # Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).


    GDP_last10 = GDP[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
                    '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                     '2014', '2015']]

    ScimEn_first15 = ScimEn[ScimEn['Rank'] <=15]

    # ScimEn_first15 
    Sci_GDP_df = pd.merge(ScimEn_first15, GDP_last10, how='inner', left_on = 'Country' , right_on='Country Name' ) 
    Sci_GDP_energy_df = pd.merge(Sci_GDP_df, energy, how='left', left_on = 'Country' , right_on='Country')

    Sci_GDP_energy_df =Sci_GDP_energy_df[ ['Country', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]


    # The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

    Sci_GDP_energy_df.set_index( 'Country', drop=True, inplace=True)

    return Sci_GDP_energy_df


  
answer_one()    








energy.shape  # (227, 4)
GDP.shape  # (264, 60)
ScimEn.shape  # (191, 8)
# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

GDP_last10 = GDP[
    [
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]
]
# GDP_last10.columns
# GDP.columns
ScimEn_first15 = ScimEn[ScimEn["Rank"] <= 15]
# ScimEn_first15
Sci_GDP_df = pd.merge(
    ScimEn_first15, GDP_last10, how="inner", left_on="Country", right_on="Country Name"
)
Sci_GDP_energy_df = pd.merge(
    Sci_GDP_df, energy, how="left", left_on="Country", right_on="Country"
)


# Sci_GDP_df.shape

Sci_GDP_energy_df.shape


Sci_GDP_energy_df = Sci_GDP_energy_df[
    [
        "Country",
        "Rank",
        "Documents",
        "Citable documents",
        "Citations",
        "Self-citations",
        "Citations per document",
        "H index",
        "Energy Supply",
        "Energy Supply per Capita",
        "% Renewable",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]
]

Sci_GDP_energy_df.columns


# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

Sci_GDP_energy_df.set_index("Country", drop=True, inplace=True)

Sci_GDP_energy_df.columns



def avg_gdp(row):
    data = row[['2006',
                '2007',
                '2008',
                '2009',
                '2010',
                '2011',
                '2012',
                '2013',
                '2014',
                '2015']]
    return pd.Series({'avgGDP': np.mean(data)})
    
def answer_three():
    Top15 = answer_one()
    Top15['avgGDP'] = Top15.apply(avg_gdp, axis=1)
    return    Top15['avgGDP'].sort_values(ascending = False)

catch = answer_three()


# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?

# This function should return a single number.

def answer_four():
    Top15 = answer_one()
    Top15['avgGDP'] = Top15.apply(avg_gdp, axis=1)
    arrangedGDP = Top15['avgGDP'].sort_values(ascending=False)
    sixthLargestAvgGDP =  arrangedGDP.index[5]
    Top15['GDPChange'] = Top15['2015'] - Top15['2006']
    
    sixthLargestAvgGDPRow  = Top15.loc[sixthLargestAvgGDP]
#     return sixthLargestAvgGDPRow
    return sixthLargestAvgGDPRow['GDPChange']
    
catch = answer_four()

catch
def answer_four():
    Top15 = answer_one()
    Top15['avgGDP'] = Top15.apply(avg_gdp, axis=1)
    arrangedGDP = Top15['avgGDP'].sort_values(ascending=False)
    sixthLargestAvgGDP =  arrangedGDP.index[5]
    Top15['GDPChange'] = Top15['2015'] - Top15['2006']
    
    sixthLargestAvgGDPRow  = Top15.loc[sixthLargestAvgGDP]
#     return sixthLargestAvgGDPRow
    return sixthLargestAvgGDPRow['GDPChange']
    
catch = answer_four()
​
def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()


 
def answer_six():
    Top15 = answer_one()
    maxRenewable = Top15['% Renewable'].max()
    rowWithMaxRenewable = Top15[Top15['% Renewable'] == maxRenewable]
    CountryWithMaxRenewable = rowWithMaxRenewable.index[0]
    
    return (CountryWithMaxRenewable, maxRenewable)
answer_six()   


def answer_seven():
    Top15 = answer_one()
    Top15 ['CitationRatio'] = Top15 ['Self-citations'] / Top15 ['Citations']
    maxCitationRatio = Top15['CitationRatio'].max()
    rowWithMaxCitationRatio = Top15[Top15['CitationRatio'] == maxCitationRatio]
    CountryWithMaxCitationRatio = rowWithMaxCitationRatio.index[0]
    return (CountryWithMaxCitationRatio, maxCitationRatio)
   
answer_seven()


def answer_nine():
    Top15 = answer_one()
    Top15['EstimatePopulation'] = Top15['Energy Supply'].divide(Top15['Energy Supply per Capita'], fill_value=0)

    Top15['Citable documents per person'] =  Top15['Citable documents'].divide(  Top15['EstimatePopulation'], 0)
    correlation_df = Top15 [['Citable documents per person', 'Energy Supply per Capita']].corr(method='pearson', min_periods=1) 
    
    return correlation_df.loc['Citable documents per person', 'Energy Supply per Capita' ]

answer_nine()


def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


 def answer_ten():
    Top15 = answer_one()
    medianRenewable  = Top15['% Renewable'].median
    return Top15['% Renewable'].sort_values()

answer_one()



eate a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.

def answer_ten():
    Top15 = answer_one().sort_values('Rank')
    medianRenewable  = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable'].apply( lambda x: 1 if x >= medianRenewable else 0)
    return (Top15['HighRenew'])

answer_ten()

def answer_ten():
    Top15 = answer_one().sort_values('Rank')
    medianRenewable  = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable'].apply( lambda x: 1 if x >= medianRenewable else 0)
    return (Top15['HighRenew'])
​
answer_ten()


def answer_eleven():
    Top15 = answer_one()
    Top15['EstimatedPopulation'] = Top15['Energy Supply'].divide(Top15['Energy Supply per Capita'], fill_value=0)

    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    

    continent_df = pd.DataFrame(list(ContinentDict.items()),columns = ['Country','Continent']) 
    continent_df.set_index('Country', inplace= True, drop=True)
    new_Top15 = pd.merge(Top15, continent_df, how='inner', left_index=True, right_index = True)
    
    new_Top15 = new_Top15[['Continent', 'EstimatedPopulation']]

    group_df = new_Top15.groupby('Continent').agg(['size','sum', 'mean', 'std'])

#    return  new_Top15.groupby('Continent')
    return group_df  


answer_eleven()
# catch = answer_eleven()
# catch

# for continent, df in catch:
#    print (df.std())  -- when there is only one country STDDEV = NaN

def answer_thirteen():
    Top15 = answer_one()
    Top15['EstimatedPopulation'] = Top15['Energy Supply'].divide(Top15['Energy Supply per Capita'], fill_value=0)

    Top15['FormattedValue'] = Top15['EstimatedPopulation'].apply(lambda x: "{:,}".format(x))
    
    return  Top15['FormattedValue']

answer_thirteen()


def answer_twelve():
    Top15 = answer_one()
    Top15['RenewableBin'] = pd.cut(Top15['% Renewable'], 5)
      

    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    

    continent_df = pd.DataFrame(list(ContinentDict.items()),columns = ['Country','Continent']) 
    continent_df.set_index('Country', inplace= True, drop=True)
   

    new_Top15 = pd.merge(Top15, continent_df, how='inner', left_index=True, right_index = True)
    new_Top15 = new_Top15[['Continent', '% Renewable', 'RenewableBin']]
    
    group_df = new_Top15.groupby(['Continent', 'RenewableBin']).agg(['count'])
    #group_df = new_Top15.groupby( 'RenewableBin').agg(['size'])
    
    return group_df


answer_twelve()
