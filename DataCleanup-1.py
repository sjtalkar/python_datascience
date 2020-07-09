# def answer_one():

# when fnctions such as mean give you an error, find unique() values and check data  Use astype to convert data
# 1) into a DataFrame with the variable name of **energy**. --done
# 2) Keep in mind that this is an Excel file, and not a comma separated values file.--done
# 3) Also, make sure to exclude the footer and header information from the datafile. --done
# 4)The first two columns are unneccessary, so you should get rid of them, --done
# 5)and you should change the column labels so that the columns are:
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`

# 6)Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule).--Done


# 8)Rename the following list of countries (for use in later questions):

# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# ---DONE

import pandas as pd
import numpy as np

energy = pd.read_excel("Energy Indicators.xls", header=15, skipfooter=38)
pd.set_option("display.max_rows", 300)
# energy.head(n=266)
# energy.shape
# energy.index
# energy.columns


energy.rename(
    columns={
        energy.columns[2]: "Country",
        energy.columns[3]: "Energy Supply",
        energy.columns[4]: "Energy Supply per Capita",
        energy.columns[5]: "% Renewable",
    },
    inplace=True,
)


energy.drop(energy.index[0], inplace=True)


energy.drop(energy.iloc[:, 0:2], inplace=True, axis=1)


# 7)For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
energy = energy.applymap(lambda x: np.nan if str(x) == "..." else x)


# 8) There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
energy["Country"] = energy["Country"].str.split("[\d\(]")  # split the index by '('

energy["Country"] = energy["Country"].str[0]
energy["Country"] = energy["Country"].str.strip()
energy["Country"]


energy["Country"] = energy["Country"].apply(
    lambda x: "South Korea" if x == "Republic of Korea" else x
)
energy["Country"] = energy["Country"].apply(
    lambda x: "United States" if "United States of America" in x else x
)
energy["Country"] = energy["Country"].apply(
    lambda x: "United Kingdom"
    if "United Kingdom of Great Britain and Northern Ireland" in x
    else x
)
energy["Country"] = energy["Country"].apply(
    lambda x: "Hong Kong"
    if "China, Hong Kong Special Administrative Region" in x
    else x
)


# Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

# Make sure to skip the header, and rename the following list of countries:

# "Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"


import pandas as pd
import numpy as np

GDP = pd.read_csv("world_bank.csv", header=4)
pd.set_option("display.max_rows", 300)
# GDP.head(n=266)
# GDP.shape
# GDP.index
# GDP.columns

energy.replace(value="South Korea", to_replace="Republic of Korea", inplace=True)
energy.replace(
    value="United States", to_replace="United States of America", inplace=True
)
energy.replace(
    value="United Kingdom",
    to_replace="United Kingdom of Great Britain and Northern Ireland",
    inplace=True,
)
energy.replace(
    value="Hong Kong",
    to_replace="China, Hong Kong Special Administrative Region",
    inplace=True,
)


energy["Energy Supply per Capita"] = energy["Energy Supply per Capita"] / (10 ** 6)


pd.set_option("display.max_rows", 500)
# energy.head(n=250)
# energy[(energy['Country'] == 'South Korea') | (energy['Country'] == 'United States') | (energy['Country'] == 'United Kingdom') | (energy['Country'] == 'Hong Kong')]
energy.head(n=250)


def answer_one():

    energy = pd.read_excel("Energy Indicators.xls", header=15, skipfooter=38)
    energy.rename(
        columns={
            energy.columns[2]: "Country",
            energy.columns[3]: "Energy Supply",
            energy.columns[4]: "Energy Supply per Capita",
            energy.columns[5]: "% Renewable",
        },
        inplace=True,
    )

    energy.drop(energy.index[0], inplace=True)

    energy.drop(energy.iloc[:, 0:2], inplace=True, axis=1)

    # 7)For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
    energy = energy.applymap(lambda x: np.nan if str(x) == "..." else x)

    # 8) There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
    energy["Country"] = energy["Country"].str.split("[\d\(]")  # split the index by '('

    energy["Country"] = energy["Country"].str[0]
    energy["Country"] = energy["Country"].str.strip()

    energy.replace(value="South Korea", to_replace="Republic of Korea", inplace=True)
    energy.replace(
        value="United States", to_replace="United States of America", inplace=True
    )
    energy.replace(
        value="United Kingdom",
        to_replace="United Kingdom of Great Britain and Northern Ireland",
        inplace=True,
    )
    energy.replace(
        value="Hong Kong",
        to_replace="China, Hong Kong Special Administrative Region",
        inplace=True,
    )

    energy["Energy Supply per Capita"] = energy["Energy Supply per Capita"] / (10 ** 6)

    GDP = pd.read_csv("world_bank.csv", header=4)
    pd.set_option("display.max_rows", 300)

    GDP.replace(value="South Korea", to_replace="Korea, Rep.", inplace=True)
    GDP.replace(value="Iran", to_replace="Iran, Islamic Rep.", inplace=True)
    GDP.replace(value="Hong Kong", to_replace="Hong Kong SAR, China", inplace=True)

    ScimEn = pd.read_excel("scimagojr-3.xlsx")

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

    ScimEn_first15 = ScimEn[ScimEn["Rank"] <= 15]

    # ScimEn_first15
    Sci_GDP_df = pd.merge(
        ScimEn_first15,
        GDP_last10,
        how="inner",
        left_on="Country",
        right_on="Country Name",
    )
    Sci_GDP_energy_df = pd.merge(
        Sci_GDP_df, energy, how="left", left_on="Country", right_on="Country"
    )

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

    # The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

    Sci_GDP_energy_df.set_index("Country", drop=True, inplace=True)

    return Sci_GDP_energy_df


answer_one()

