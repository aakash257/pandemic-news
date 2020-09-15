import scrape, filter, save

def script():

    url = 'https://lite.cnn.com/en'
    news_dict = scrape.scrape_headline(url)
    pandemic_news_dict = filter.filter_pandemic_news(news_dict)
    save.save_dictionary_to_csv(pandemic_news_dict)

    article_text_list = []
    for key in pandemic_news_dict:
        article_text = scrape.scrape_article(key) #key is article link
        article_text_list.append(article_text)

    save.save_articles_to_txt(article_text_list)

    return
