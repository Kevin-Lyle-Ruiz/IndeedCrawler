from bs4 import BeautifulSoup
from classes import PageElements
from functions import parsePage, sendEmail
import requests, csv

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

#Creating BeautifulSoup object
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Looking for all the cards container job information
job_elems = soup.find_all('div', class_='jobsearch-SerpJobCard')

#Creating CSV page with headings to put data under
with open('IndeedResults.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Location', 'Link'])

#Creating an object the contains the required elements to perform page crawling
indeedPageElements = PageElements(URL, job_elems, jobKeywords)

print('\nCrawling...')
parsePage(indeedPageElements,)

sendEmail()