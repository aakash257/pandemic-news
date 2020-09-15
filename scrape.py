import requests
from bs4 import BeautifulSoup
import clean as cleantext

class myDict(dict):
    """create an empty dictionary and append key-value pairs"""

    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

def scrape_headline(news_link):
    """
    function to scrape the headlines from a simple news website

    :return:    a dictionary with key as html link of the source and
                value as the text in the headline of the news in the html link
    """
    #Headlines
    #URL = 'https://lite.cnn.com/en'
    page = requests.get(news_link)
    soup = BeautifulSoup(page.content, 'html.parser')

    daily_news_headline_dict = myDict()

    for link in soup.find_all('a'):
        key = 'https://lite.cnn.com'+link.get('href')
        text = cleantext.create_cleanerDoc(link.get_text('href'))
        daily_news_headline_dict.add(key, text)
            #print(daily_news_headline_dict)

    return daily_news_headline_dict

def scrape_article(article_link):
    """
    function to clean text in the news article's html link

    :param article_link:    url of a news article
    :return:    a cleaner text of the news article in the article_link
    """
    page = requests.get(article_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(page.text)
    para_list = []
    for para in soup.find_all('p'):
        para_list.append(para.get_text())

    article_text = ' '.join(para_list)
    article_cleantext = cleantext.create_cleanerDoc(article_text)

    return article_cleantext
