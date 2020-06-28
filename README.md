# Indeed Job Crawler

This program searches through [Indeed.com](https://indeed.com) for job listings. The jobs to look for as well the 
location to look for the jobs is up to the user. The search results is then output to a CSV file and then the user 
is then given the option to send the results to an email of the user's choice.

**Note**: The search query is strict in that if a user is searching for **Software Developer**, the crawler will 
          only output the results to the CSV file if the job title contains the words **Software** or **Developer**,
          ignoring case-sensitivity.


## Prerequisites

* [Python3](https://www.python.org/downloads/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/#Download) - Python library for parsing structured data
* [Pandas](https://pandas.pydata.org/getting_started.html) - Python library used to read CSV file and format for Email

## Getting Started

1. Download respository to your preferred location
2. Open a terminal and go into the repository directory
3. Run command ```python3 crawler.py```

**Important Note**: To send an email using the program, you must have an email that has **Access for less secure apps** enabled in the setting.
                    It is recommended to create a new email for this functionality as enabling this setting makes your email less secure.
                    
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
