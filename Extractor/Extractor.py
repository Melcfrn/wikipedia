
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
            raise 'URL does not exist'

        return bs(html, 'html.parser')

    def getAllWikitable(self,soup) : 
        """_summary_

        Args:
            soup (_type_): bs4.element, html script of the Wikipage

        Returns:
            _type_: list of all tables present in the Wikipage
        """
        tableslist = soup.find_all("table",{"class":"wikitable"})
        if tableslist == [] :
            raise Exception('no table disponible')
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
        try : 
            html_script = list(parents[self.index])
        except :
            raise 'Index out of range'
        return html_script


## A supprimer


Try = Extractor()


html = Try.get_Document()
All = Try.getAllWikitable(soup=html)
Parents = Try.getAllParentsWikitable(tableslist=All)
with  open("python.txt", "w", encoding="utf-8") as file:
    file.write(str(All))
    file.write("  \n   ")
    file.write("-----")
    file.write("  \n   ")
    file.write(str(Parents))
    file.write("  \n   ")
    file.write("+++++")
    file.close()
