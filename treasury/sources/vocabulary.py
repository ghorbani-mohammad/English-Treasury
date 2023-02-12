import requests
from bs4 import BeautifulSoup as BS


class VocabularyAPI:
    URL = "https://www.vocabulary.com"

    def get_short_description(self, word):
        resp = requests.get(f"{self.URL}/dictionary/{word}")
        doc = BS(resp.text, "html.parser")
        return doc.find("p", {"class": "short"})

    def get_long_description(self, word):
        resp = requests.get(f"{self.URL}/dictionary/{word}")
        doc = BS(resp.text, "html.parser")
        return doc.find("p", {"class": "long"})
