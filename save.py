from datetime import date
import os
today = date.today()
todays_date = today.strftime("%d %B %Y")

#save pandemic news dictionary to a csv file
def save_dictionary_to_csv(news_dict):
    """
    function to save pandemic news dictionary in a csv file

    :param news_dict:   a dictionary of key-value pairs as news source's html
                        link and headline text
    """
    import pandas as pd
    df = pd.DataFrame(data=news_dict, index=[0])
    df = (df.T)

    df.to_csv('pandemic_news_headlines.csv', mode = 'a',
              header = ['Headlines for '+str(todays_date)])

def save_articles_to_txt(articles_list):
    """
    function to save list of articles in a text file

    :param articles_list:   list of articles' texts
    """
    iPath = os.getcwd()
    txtFileName = str(today.strftime("%d_%B_%Y"))+'.txt'

    newFilePath = iPath+'\\'+'pandemic_news_articles'+'\\'+txtFileName
    with open(newFilePath, 'w') as newdocFile:
        for articles in articles_list:
            newdocFile.writelines(articles + '\n')
    return
