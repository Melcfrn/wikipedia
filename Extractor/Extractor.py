
import requests
from bs4 import BeautifulSoup as bs

class Extractor():
    def __init__(self,url = "https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units", index = None):
        self.url = url
        self.index = index
    
    def get_Document(self) :
        """_summary_

        Returns:
            _type_: bs4.element, html file of the Wikipage
        """
        try :
            html = requests.get(self.url).text
        except :
            raise Exception('URL do not exist')
            
        return bs(html, 'html.parser')

    def getAllWikitable(self,soup) : 
        """_summary_

        Args:
            soup (_type_): bs4.element, html script of the Wikipage

        Returns:
            _type_: list of all tables present in the Wikipage
        """
        tableslist = soup.find_all("table",{"class":"wikitable"})
        return tableslist
    
    def getAllParentsWikitable(self,tableslist) :
        """_summary_
        Filter the tables, in order to keep only the parents tables
        Args:
            tableslist (_type_): list of all tables present in the Wikipage

        Returns:
            _type_: List of Parents tables 
        """
        parents = tableslist[0].parent("table",{"class":"wikitable"})
        return parents
    
    def getWikitable(self,parents) :
        """_summary_

        Args:
            parents (_type_): List of Parents tables 

        Returns:
            _type_: _description_
        """
        if len(parents) < self.index :
            raise Exception('Index to long')
        return list(parents[self.index])

    