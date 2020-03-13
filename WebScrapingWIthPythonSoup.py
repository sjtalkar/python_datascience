from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.cdc.gov/coronavirus/2019-ncov/travelers/index.html")
print(source.ok)
#httpbin.org\

print (source.url)
#################################My PROJECT -- EXTRACTING URLS #######################################################################################
######################################################################################################################################################

#with open("C:\PYTHONDATASCIENCE\CDCData.html") as fileRef:
#    soup = BeautifulSoup(fileRef,'lxml')
#Watch scraping of youtube id here : https://www.youtube.com/watch?v=ng2o98k983k

source = requests.get("https://www.cdc.gov/coronavirus/2019-ncov/travelers/index.html").text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

removeTag = ['path']
#Clean up all path tags

for tag in soup.find_all(True):
    if tag.name.lower() in removeTag:
       # removeTag tags are removed in their entirety
       tag.extract()

tagNameList = [tag.name for tag in soup.findAll(True)]
tagNameList.sort()
print("Now the tags are {}".format(set(tagNameList)))
print()

findWhat = ['a', 'img']
getImages = [image for image in soup.find_all(findWhat, href=True)]
    
for image in getImages:
    print("URL for link is: {}".format(image['href']))   
###########################################################################################################################################################
###################################SCRAPING WITH REGEX#####################################################################################################

import os
import re
import requests
from bs4 import BeautifulSoup


url = 'https://bitinfocharts.com/comparison/bitcoin-transactions.html'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
script_tag = soup.findAll('script')[5]
script_text = script_tag.text


pattern = re.compile(r'\[new Date\("\d{4}/\d{2}/\d{2}"\),\d*\w*\]')
records = pattern.findall(script_text)


def parse_record(record):
    date = record[11:21]
    value = record[24:-1]
    return [date,value]

transactions = []

for record in records:
    transactions.append(parse_record(record))
	
print(transactions)


###########################################################################################################################################################
###################################SCRAPING   AND STORING IN CSV#####################################################################################################

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()	