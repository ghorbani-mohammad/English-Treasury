import requests
from bs4 import BeautifulSoup as BS


class VocabularyAPI:
    URL = "https://www.vocabulary.com"

    def get_short_definition(self, word):
        resp = requests.get(f"{self.URL}/dictionary/{word}")
        doc = BS(resp.text, "html.parser")
        return doc.find("p", {"class": "short"}).text

    def get_long_definition(self, word):
        resp = requests.get(f"{self.URL}/dictionary/{word}")
        doc = BS(resp.text, "html.parser")
        return doc.find("p", {"class": "long"}).text

    def get_definitions(self, word):
        resp = requests.get(f"{self.URL}/dictionary/{word}")
        doc = BS(resp.text, "html.parser")
        short_definition = doc.find("p", {"class": "short"}).text
        long_definition = doc.find("p", {"class": "long"}).text
        return short_definition, long_definition
