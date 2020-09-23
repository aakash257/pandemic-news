import scrape, filter, save

url = 'https://lite.cnn.com/en'
news_dict = scrape.scrape_headline(url)
pandemic_news_dict = filter.filter_pandemic_news(news_dict)
save.save_dictionary_to_csv(pandemic_news_dict)

article_text_list = []
input_unit = 'full'
for key in pandemic_news_dict:
    if input_unit != 'full':
        article_text = scrape.scrape_article(key, input_unit) #key is article link
        article_text_list.extend(article_text)
    elif input_unit == 'full':
        article_text = scrape.scrape_article(key, input_unit) #key is article link
        article_text_list.append(article_text)

save.save_articles_to_txt(article_text_list, input_unit)
