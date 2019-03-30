
import json
import requests
from bs4 import BeautifulSoup



BASE = "https://news.google.com/news"
TOPICS = ["WORLD", "NATION", "BUSINESS", "TECHNOLOGY", "ENTERTAINMENT", "SPORTS", "SCIENCE", "HEALTH"]
TOPIC_URL = "/headlines/section/topic"
GEO_URL = "/headlines/section/geo"

QUERY = "https://news.google.com/rss/search?pz=1&cf=all&q=%22Economy%22&cf=all&scoring=n&hl=en-GB&gl=GB&ceid=GB:en"


class GNews: 
	def __init__(self, edition='United States (English)', topic='top stories', location=None, query=None, language='english'):
        self.edition = edition
        self.topic = topic
        self.location = location
        self.query = query
        self.language = language
        self.requestparams = {'output': 'atom',
                              'ned': self.edition,
                              'topic': self.topic,
                              'geo': self.location,
                              'q': self.query,
                              'hl': self.language}
    def send_request: 

        resp = requests.get(BASE, params=self.params)
        soup = BeautifulSoup(resp.content, 'html5lib')

        articles = self.scrape_feed(soup)


    	entries = soup.findAll('entry')
    	news_articles = []

        for entry in entries:
            article = {}
            article['title'] = entry.title.text
            article['link'] = entry.link['href']
            article['releasedAt'] = entry.updated.text
            articles.append(article)

        return articles

