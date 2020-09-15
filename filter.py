covid_wordset = ['covid', 'pandemic']

class myDict(dict):
    """
    create an empty dictionary and append key-value pairs
    """

    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

pandemic_daily_news_dict = myDict()
def filter_pandemic_news(news_dict):
    """
    function to filter pandemic news from all types of news

    :param news_dict:   a dictionary of key-value pairs as news source's html
                        link and headline text
    :return:            a dictionary of key-values pairs as news source's html
                        link and pandemic news headline
    """
    for key in news_dict:
        news_text = news_dict[key]
        news_text_wordlist = news_text.split()
        if len(set(covid_wordset).intersection(set(news_text_wordlist)))>=1:
            pandemic_daily_news_dict.add(key, news_text)

    return pandemic_daily_news_dict
