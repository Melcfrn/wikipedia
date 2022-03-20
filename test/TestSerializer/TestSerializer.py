import pytest
import os
import sys
sys.path.append(os.getcwd() + '/main')
from Serializer.Serializer import Serializer
from Extractor.Extractor import Extractor
from Convertor.Convertor import Convertor


class TestSerializer():

    def test_assertPath(self):
        serial = Serializer([], "", 0)
        path0 = "voici_un?test"
        path1 = "voici-un<test"
        path2 = "voici-un|test"
        assert not (serial.assertPath(path0) * serial.assertPath(path1) \
            * serial.assertPath(path2))


    def test_serialize(self):
        wiki = "https://en.wikipedia.org/wiki/Comparison_(grammar)"
        header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
        Try = Extractor(wiki)
        a = Try.get_Document()
        tables = Try.getAllWikitable(soup=a)
        conv = Convertor(tables)
        sortie_conv = conv.allTablesTo2D()
        serial = Serializer(sortie_conv[0], wiki, 0)
        serial.serialize("./test/TestSerializer")

        page=os.path.split(wiki)[1]
        with open(os.getcwd() + '/test/TestSerializer/serializeTest.csv', 'r') as csv1, \
        open(os.getcwd() + '/test/TestSerializer/{}-{}.csv'.format(page, 0), 'r') as csv2:
            import1 = csv1.readlines()
            import2 = csv2.readlines()

        assert import1 == import2
