import pytest
from Extractor import Extractor

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
