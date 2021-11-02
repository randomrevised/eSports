# imports
import datetime

# helper group class
class Group:
    pass

# helper class
class Helper:
    """
    init and str methods
    """
    def __init__(self, name, id, group=None): # nickname, discord id
        self.name = name
        self.id = id # basic attributes
        #self.group.helpers[name] = id # update helpers group
        self.articles = [] # articles
        # add start time
        self.join_date = datetime.datetime.now().isoformat()
        # add earnings
        self.total_learnings = 0
        self.max_earnings = 0
        self.earnings = 0
    
    def __str__(self):
        # return Name, ID, Group, Date Joined, Total Earnings, Max Earnings
        return """Basic Info\n\nName: {}\nID: {}\nGroup: {}\nDate Joined: {}
        \n\nStats\n\nArticles Written: {}
        \nTotal Earnings: {} crystals\nMax Earnings: {} crystals""".format(self.name, self.id, "WIP", self.join_date[:10], len(self.articles), self.total_learnings, self.max_earnings)

    """
    Earnings Methods: add earnings, reset earnings, update max earnings
    """
    def add_earnings(self, article):
        # add earnings
        self.earnings += article.earnings
        self.total_learnings += article.earnings

    def reset_earnings(self):
        # reset earnings
        self.earnings = 0

    def update_earnings(self):
        if self.earnings > self.max_earnings:
            self.max_earnings = self.earnings
        self.reset_earnings()

# article class
class Article:
    """
    Article Types:
    Short - 40000 crystals
    Medium - 60000 crystals
    Long - 80000 crystals
    """

    def __init__(self, id, type, author, title=""):
        # create date, title, author, type
        self.id = id
        self.url = "https://tankisport.com/article/{}".format(self.id) # id & url
        self.type, self.author = type, author # type & author
        self.title, self.date =  title, datetime.datetime.now().isoformat() # title and date
        # add article to author list
        self.author.articles.append("{}".format(self.url))
        # determine how much article earns and add total to author's pay
        if self.type == "Short":
            self.earnings = 40000
        elif self.type == "Medium":
            self.earnings = 60000
        elif self.type == "Long":
            self.earnings = 80000
        self.author.add_earnings(self)
        

    def __str__(self):
        # return URL, Author, Date
        return "Link: {}\nAuthor: {}\nPublished: {}".format(self.url, self.author.name, self.date[:10])


