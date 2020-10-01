from bs4 import BeautifulSoup
from urllib import parse as url_parser
import requests
from FitGirlScraper.scraper.article import Article


def get_html(url):
    r = requests.get(url)
    return r.content


def get_magnet(url):
    soup = BeautifulSoup(get_html(url), "html.parser")
    for li_soup in soup.find_all("a"):
        if str(li_soup['href']).startswith('magnet'):
            return li_soup['href']
    return None


class Scraper:
    def __init__(self, search_query):
        self.url = 'https://fitgirl-repacks.site/?s=' + url_parser.quote(search_query)
        self.elements = []

    def get_elements(self):
        soup = BeautifulSoup(get_html(self.url), "html.parser")
        for article_soup in soup.find_all("article"):
            title = article_soup.header.h1.a.text
            link = article_soup.header.h1.a['href']
            magnet = get_magnet(link)
            if magnet is None:
                continue
            self.elements.append(Article(title, link, magnet))

        return self.elements
