import sys
import requests
import os
import pickle
from bs4 import BeautifulSoup as BS
BASE_URL = "http://www.cnn.com/"
CAT = ["world", "opinions", "health","entertainment", "travel","us"]

def _link_filter(link):
    return True

def _get_links(url):
    source_code = requests.get(url)
    parsed_context = BS(source_code.text, "html.parser")
    headlines = # h3, cd__headline
    links = []
    # links = list(filter(_link_filter, links))
    return links

def _news_scrapper(url):
    source_code = requests.get(url)
    parsed_context = BS(source_code.text, "html.parser")
    try:
        title = # get title
        sentences = # get sentences
    except AttributeError:
        print(url)
        return {}
    return {'title':title, 'content':''.join(sentences)}

def _get_data():
    y = []
    urls = []
    # get links for each article

    # get content
    articles = list(map(_news_scrapper, urls))

    # remove fail
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
