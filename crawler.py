from bs4 import BeautifulSoup
from assets.classes import PageElements
from assets.functions import parsePage, dataToCSV, sendEmail, truncateData
import requests

print('What job are you looking for?')
jobRequest = input()
print('\nWhat location would you like to search?')
locationRequest = input()

#Keywords to look for when parsing
jobKeywords = jobRequest.split(' ')

#Formatting string for URL input
job = jobRequest.replace(" ", "+")
location = locationRequest.replace(" ", "+")

URL = 'https://www.indeed.com/jobs?q=' + job + '&l=' + location

# Creating BeautifulSoup object
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Looking for all the cards container job information
job_elems = soup.find_all('div', class_='jobsearch-SerpJobCard')

# Creating an object the contains the required elements to perform page crawling
indeedPageElements = PageElements(URL, job_elems, jobKeywords)

print('\nCrawling...')

# Parsing page and putting into database
parsePage(indeedPageElements,)

# CSV option
dataToCSV()

# Print option
sendEmail()

# Deleting data from table
truncateData()