import pytest
import os
import sys
sys.path.append(os.getcwd() + '/main')
from Serializer.Serializer import Serializer
from Extractor.Extractor import Extractor
from Convertor.Convertor import Convertor
from bs4 import BeautifulSoup as bs

class TestExtractor():
    def test_get_Document(self):

        BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"

        extractor = Extractor(BASE_WIKIPEDIA_URL)

        doc = None
        try :
            doc = extractor.get_Document()
        except :
            raise "Unable to connect to wikipedia"

        assert doc

    def test_getAllWikitable(self):

        extractor = Extractor(url="https://en.wikipedia.org/wiki/Comparison_(grammar)")
        soup = extractor.get_Document()

        tables = None
        tables = extractor.getAllWikitable(soup)

        assert len(tables) == 6
