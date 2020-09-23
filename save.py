from datetime import date
from datetime import datetime
import os
today = date.today()
todays_date = today.strftime("%d_%B_%Y")

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

    #check whether today's headlines are saved
    lastmod = os.stat('pandemic_news_headlines.csv').st_mtime
    file_modified_date = datetime.fromtimestamp(lastmod).strftime("%d_%B_%Y")
    if todays_date != file_modified_date:
        df.to_csv('pandemic_news_headlines.csv', mode = 'a',
                  header = ['Headlines for '+str(todays_date)])
    else:
        print("today's headlines are already saved")

def save_articles_to_txt(articles_list, input_unit):
    """
    function to save list of articles in a text file

    :param articles_list:   list of articles' texts
    :param input_unit:      input unit can be a sentence (sent), paragraph
                            (para), or an article (full)
    """
    iPath = os.getcwd()
    txtFileName = str(todays_date)+'_'+input_unit+'.txt'

    newFilePath = iPath+'\\'+'pandemic_news_articles'+'\\'+txtFileName
    with open(newFilePath, 'w') as newdocFile:
        for articles in articles_list:
            newdocFile.writelines(articles + '\n')
    return
