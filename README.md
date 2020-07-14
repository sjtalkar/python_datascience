# Data Cleaning and Interpretation using Pandas 
### University of Michigan Introduction to Data Science in Python


######  Jupyter notebook for Housing price drop comparison during one recession period: HousingPricesUniversityTownComparison.ipynb


#### Assignment builds skills in these key areas: 
* Jupyter Notebook : 
  * Advantages having markdown and code segments and so commenting can be inline without adding any distaraction
  * Requirements can be specified in detail ina markdown section
  * Python syntax and Time series functions can be inferred through extension that can be added for auto complete and function details
  * Output is visible and stored below each cell run

* Reads from a text, CSV and excel spreadsheet with their unique data cleanup challenges 
  * Text
    Hierarchically presented data with state followed by university towns to be converted to state, city tuples
    The states and the towns have to be extracted from a string that includes names of colleges and additional information
  * Excel
    Header and footers to be eliminated along with columns for annual GDP to retain only quarterly GDP

* Using Map to replace abbreviations with State names
* Manipulation of columns and indexes as independent of data arrays
* Converting column names to quarterly periods so that a quarterly mean can be derived with a one statement resample call
  temp_zillow = temp_zillow[columns_we_need].resample('QS',axis=1).mean()
* Selection of columns based on  chronological order 
* Replacing dates into their respective quarters so that colun names reflect quarters
* Adding additional columns using DataFrame.assign
* Use of () to create Pandorable code in Jupyter notebook
* Using Left join between two dataframes

#### Three checks I perform after reading in the data:
To eliminate headers
.head()

To eliminate grand totals and additional footers
.tail()

To get sense of number of rows and columns
.shape 


# Other programs in this repository are smaller projects from other Coursera courses :
## Implementing Python programs for DataScience course application

The files of interest in this project are the ones that set up the tools that can be repeatedly used in datascience

The file ImageAndTextAndColorTines.Py was developed as an exercise to create a collage of images canvas with varying hues

The file WebScrapingWithPythonSoup.py utilizes requests library to fetch a requested URL, parses the HTML using BeautifulSoup and extracts HTML elements out of web pages

The file DirectoryAndFileOperations.py is used to rename files that are currently sorted alphabetically, so that the number of the file appears before any string





