from bs4 import BeautifulSoup
from classes import PageElements
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests, csv, smtplib, ssl, getpass, io
import pandas as pd

#Parses page and adds contents to CSV file
def parsePage(PageElements):
    domain = 'https://indeed.com'
    job_elems = PageElements.getJobElems()
    jobKeywords = PageElements.getJobKeywords()

    PageElements.printURL()
    for jobs in job_elems:
        title = format(jobs.find('a', class_='jobtitle').text.strip())

        #Checks to see if job title contains job keywords
        if (containsAllWords(title, jobKeywords)):
            company = format(jobs.find('span', class_='company').text.strip())

            link = jobs.find('a')['href']
            link = domain + link

            #Checking to see if job location is using div or span tag
            if jobs.find('span', class_='location') is not None:
                location = format(jobs.find('span', class_='location').text.strip())
            else:
                location = format(jobs.find('div', class_='location').text.strip())

            with open('IndeedResults.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([title, company, location, link])

    next_page(PageElements)

#Checks to see if next page exists
def next_page(PageElements):

    #URL for next page
    PageElements.incrementSearchIndex(10)
    search_url = PageElements.generateSearchURL()

    page = requests.get(search_url)

    #Detemines if the search url is valid and requesting okay
    if (page.status_code == requests.codes.ok):
        PageElements.setURL(search_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        #Checking to see if the first page has additional pages to search
        if (soup.find('ul', class_='pagination-list') != None):
            list_elems = soup.find('ul', class_='pagination-list')
            last_page = list_elems.find_all('li')[-1]

            #Checking to see if on the last page
            if (last_page.find('b') == None):
                job_elems = soup.find_all('div', class_='jobsearch-SerpJobCard')

                PageElements.setJobElems(job_elems)
                parsePage(PageElements)
            else:
                print('Completed!')
        else:
            print('Completed!')

#Checks to see if job title contains all keywords
def containsAllWords(word, keywords):
    for keyword in keywords:
        if not(keyword.lower() in word.lower()):
            return False
    return True

#Sends email with job data if requested
def sendEmail():
    print('\nDo you want to send yourself an email? (y/n)')
    print('NOTE: You must have a sender email that allows access from less secure apps!')

    answer = input().lower()

    #Validation for user input
    while (answer not in {'y', 'n'}):
        print('\nInvalid input!')
        print('Do you want to send yourself an email? (y/n)')
        answer = input()

    #If user answer no, program ends
    #Else, program asks for credentials before reading CSV file and sending email
    if (answer == 'n'):
        print('\nGoodbye!')
    else:
        #Asking for credentials
        print('\nPlease enter your login credentials for sender email')
        print('E-mail:', end=' ')
        sender_email = input()
        password = getpass.getpass()

        print('\nEnter the receiver email:', end=' ')
        receiver_email = input()

        #Reads csv using pandas and converts csv to html string
        str_io = io.StringIO()
        df = pd.read_csv('IndeedResults.csv')
        df.to_html(buf=str_io)
        table_html = str_io.getvalue()
        
        #Creating the message for the email
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Indeed Crawler Results'
        message['From'] = sender_email
        message['To'] = receiver_email

        text = '''\
        Indeed Crawler Results'''

        html = '''\
        <html>
            <body>
                <p>{table_html}</p>
            </body>
        </html>
        '''.format(table_html=table_html)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        message.attach(part1)
        message.attach(part2)    
        
        #Sending the email
        port = 465
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print('\nEmail Sent!')