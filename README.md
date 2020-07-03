# Indeed Job Crawler

This program searches through [Indeed.com](https://indeed.com) for job listings. The jobs to look for as well the 
location is up to the user. The search results are put into a database, which the CSV receives data from and then the user 
is then given the option to send the results to an email of the user's choice.

**Note**: The search query is strict in that if a user is searching for **Software Developer**, the crawler will 
          only output the results to the CSV file if the job title contains the words **Software** or **Developer**,
          ignoring case-sensitivity.

## Prerequisites

* [Python3](https://www.python.org/downloads/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/#Download) - Python library for parsing structured data
* [Pandas](https://pandas.pydata.org/getting_started.html) - Python library used to read CSV file and format for Email
* [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter that Python uses to connect to the database

## Getting Started

1. Download respository to your preferred location
2. Open a terminal and go into the repository directory
3. Run command ```python3 crawler.py```
