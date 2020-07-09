import numpy as np
from bs4 import BeautifulSoup
import requests as req
import pandas as pd

URL = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
whatDidIGet = pd.read_html(URL)

allCountriesTable = whatDidIGet[1]
# print(allCountriesTable)
print(allCountriesTable.iloc[0])
