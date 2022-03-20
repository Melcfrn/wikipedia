import pytest
import os
import sys
sys.path.append(os.getcwd() + '/main')
from Serializer.Serializer import Serializer
from Extractor.Extractor import Extractor
from Convertor.Convertor import Convertor

class TestConvertor():
    def test_allTablesTo2D(self):
        wiki = "https://en.wikipedia.org/wiki/Comparison_(grammar)"
        header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
        Try = Extractor(wiki)
        a = Try.get_Document()
        tables = Try.getAllWikitable(soup=a)

        conv = Convertor(tables)
        sortie_conv = conv.allTablesTo2D()

        assert len(sortie_conv) == 6
