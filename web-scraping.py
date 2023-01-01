## Programa para encontrar notícias do Globo.com

import requests
from bs4 import BeautifulSoup

def get_news():
    url = 'https://www.globo.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    noticias = soup.find_all('a')
    tgt_class1 = 'post__title'
    tgt_class2 = 'post-multicontent__link--title__text'

    news_dict = {}
    for noticia in noticias:
        if (noticia.h2 != None) and (noticia.h2.get('class') != None):
            if tgt_class1 in noticia.h2.get('class'):
                news_dict[noticia.h2.text] = noticia.get('href')
            if tgt_class2 in noticia.h2.get('class'):
                news_dict[noticia.h2.text] = noticia.get('href')
    return news_dict


news = get_news()

print(news.keys())