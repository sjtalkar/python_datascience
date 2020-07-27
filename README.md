# Data Cleaning and Interpretation using Pandas 

<details>
  <summary markdown="span">Assignments completed for courses listed here</summary>
      <li>1. University of Michigan Introduction to Data Science in Python</li>
      <li>2. University of California Berkeley : Foundations of Data Science: Inferential thinking by resampling</li>
</details>

<details>
  <summary markdown="span">Jupyter Notebooks with Code and further information</summary>
      <li><a href = 'https://github.com/sjtalkar/DataCleaningAndTTest'>1. University of Michigan Introduction to Data Science in Python</a></li>
      <li>2. University of California Berkeley : Foundations of Data Science: Inferential thinking by resampling</li>
</details>


###  [Jupyter notebook for Housing price drop comparison during one recession period: HousingPricesUniversityTownComparison.ipynb](https://github.com/sjtalkar/DataCleaningAndTTest)
###  [Jupyter notebook Template for all future datacleaning projects: TemplateFileForDataCleaning.ipynb](https://github.com/sjtalkar/StartHereTemplates/blob/master/TemplateFileForDataCleaning.ipynb)
###  [Jupyter notebook for visualizations such as barplots and interactivity using widgets and animation: CustomVisualization.ipynb ](https://github.com/sjtalkar/VisualizationUsingMatplotlib/blob/master/CustomVisualization.ipynb)


#### Assignment builds skills in these key areas: 

* Jupyter Notebook : 
  * Advantage is that code reads like a document : Having markdown and code segments in separate cells and so commenting can be inline and yet does not distract
  * Requirements can be specified in detail in a markdown section
  * Can add extensions for auto complete and function details such as Hinterland
  * Output is visible and stored below each cell run

* Reads from a text, CSV and excel spreadsheet with their unique data cleanup challenges 
  * Text
    * Hierarchically presented data with state followed by university towns to be converted to state, city tuples
    * The states and the towns have to be extracted from a string that includes names of colleges and additional information
  * Excel
    * Header and footers to be eliminated along with columns for annual GDP to retain only quarterly GDP

* Using Map to replace abbreviations with State names
* Manipulation of columns and indexes as arrays independent of data
* Converting column names to quarterly periods so that a quarterly mean can be derived with a one statement resample call
  temp_zillow = temp_zillow[columns_we_need].resample('QS',axis=1).mean()
* Selection of columns based on  chronological order 
* Replacing dates into their respective quarters so that column names reflect quarters
* Adding additional columns using DataFrame.assign
* Use of () to create Pandorable code in Jupyter notebook, usage of assign, query....
* Using Left join between two dataframes

#### Three checks I perform after reading in the data:
To eliminate headers
.head()

To eliminate grand totals and additional footers
.tail()

To get sense of number of rows and columns
.shape 


# An ongoing project I am working on is tracking worldwide COVID data from the PDF printed out by WHO
[Pandas working of WHO covid PDF data](https://github.com/sjtalkar/ComparisonStudyPowerBIAndPandas)

[This project follows Gil Raviv's bog on finding insights into worldwide Covid data.](https://datachant.com/2020/07/16/import-who-covid-19-data-from-pdf/?mc_cid=548415d80c&mc_eid=11642bb66a)


# Other programs in this repository are smaller projects from other Coursera courses :
## Implementing Python programs for DataScience course application

The files of interest in this project are the ones that set up the tools that can be repeatedly used in datascience

The file WebScrapingWithPythonSoup.py utilizes requests library to fetch a requested URL, parses the HTML using BeautifulSoup and extracts HTML elements out of web pages

The file DirectoryAndFileOperations.py is used to rename files that are currently sorted alphabetically, so that the number of the file appears before any string





