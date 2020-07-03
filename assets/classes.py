class PageElements(object):
    def __init__(self, URL, job_elems, jobKeywords):
        self.URL = URL
        self.job_elems = job_elems
        self.jobKeywords = jobKeywords

        self.searchBase = self.URL + '&start='
        self.search_index = 0
        self.search_url = None

    #Setter functions
    def setURL(self, URL):
        self.URL = URL

    def setJobElems(self, job_elems):
        self.job_elems = job_elems

    def setJobKeywords(self, jobKeywords):
        self.jobKeywords = jobKeywords


    #Getter functions
    def getURL(self):
        return self.URL

    def getJobElems(self):
        return self.job_elems

    def getJobKeywords(self):
        return self.jobKeywords
        

    #Increments search index by the increment amount
    def incrementSearchIndex(self, increment):
        self.search_index += increment

    #Combines the search URL base and search index. Returns the search URL
    def generateSearchURL(self):
        self.search_url = self.searchBase + str(self.search_index)
        return self.search_url

    #Prints URL that is currently being searched
    def printURL(self):
        print(self.URL)