import sys
import requests
import os
import pickle
from bs4 import BeautifulSoup as BS
BASE_URL = "http://www.cnn.com/"
CAT = ["world", "opinions", "health","entertainment", "travel","us"]

def _link_filter(link):
    return link[0] == '/' and link.find('/videos') != 0 and link.find('/profile') != 0

def _get_links(url):
    source_code = requests.get(url)
    parsed_context = BS(source_code.text, "html.parser")
    headlines = parsed_context.findAll('h3',{'class':'cd__headline'})
    links = [headline.find('a').get('href') for headline in headlines]
    #v1
    # links = [link for link in links if link[0] =='/']
    # v2
    # links = list(filter(lambda x:x[0]=='/', links))
    # v3
    links = list(filter(_link_filter, links))
    return links

def _news_scrapper(url):
    source_code = requests.get(url)
    parsed_context = BS(source_code.text, "html.parser")
    try:
        title = parsed_context.find('h1').text
        sentences = [p.getText() for p in
                 parsed_context.findAll('div',{'class':'zn-body__paragraph'})]
    except AttributeError:
        print(url)
        return {}
    return {'title':title, 'content':''.join(sentences)}

def _get_data():
    y = []
    urls = []
    for cat in CAT:
        for link in _get_links(BASE_URL+cat):
            y.append(cat)
            urls.append(BASE_URL+link)
    # v1
    articles = []
    for url in urls:
        articles.append(_news_scrapper(url))
    # v2
    # articles = [_news_scrapper(url) for url in urls]

    # v3
    articles = list(map(_news_scrapper, urls))

    while {} in articles:
        idx = articles.index({})
        del y[idx], urls[idx], articles[idx]

    return y, urls, articles

def _save_data(d):
    for k, v in d.items():
        with open(k+'.pkl', 'wb') as f:
            pickle.dump(v, f)

# y, urls, articles = load_data('y','urls','articles')
def load_data(*keys):
    ans = []
    for k in keys:
        with open(k+'.pkl', 'rb') as f:
            ans.append(pickle.load(f))
    return ans

def main():
    y, urls, articles = _get_data()
    _save_data({'y':y, 'urls':urls, 'articles':articles})


if __name__ == "__main__":
    main()
