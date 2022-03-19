# import pandas as pd
# import requests
# from bs4 import BeautifulSoup as bs
#
#
# #test = pd.read_html("https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units", attrs={"class": "wikitable"})
# #parant = test[0].parent("table",{"class":"wikitable"})
#
#
#
#
# # Open the HTML in which you want to make changes
# html = requests.get("https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units").text
#
# # Parse HTML file in Beautiful Soup
# soup = bs(html, 'html.parser')
#
# # Give location where text is stored which you wish to alter
# unordered_list = soup.find_all("table",{"class":"wikitable"})
# unordered_list2 = []
# parentl = []
#
# parents = unordered_list[0].parent("table",{"class":"wikitable"})
#
# for i in unordered_list :
#     parent = i.parent("table",{"class":"wikitable"})
#     if parent not in parentl :
#         parentl.append(parent)
#
#
# for i in unordered_list :
#     a = [i]
#     if a in parentl :
#         unordered_list2.append(i)
#
#
# liste = []
# liste2 = []
# for i in parents :
#     if i not in liste :
#         liste.append(i)
#     else :
#         if i not in liste2 :
#             liste2.append(i)
#
# test = type(parents[0])
#
# print(len(liste))
# with  open("python.txt", "w", encoding="utf-8") as file:
#     #file.write(str(unordered_list))
#     file.write("  \n   ")
#     file.write("-----")
#     file.write("  \n   ")
#     file.write(str(soup))
#     file.write("  \n   ")
#     file.write("+++++")
#     file.write("  \n   ")
#     file.write(str(html))
#     file.close()








from itertools import product
from queue import Empty
from urllib import request
from bs4 import BeautifulSoup
from Extractor.Extractor import Extractor
from Convertor.Convertor import Convertor
import os
import codecs
import numpy as np

wiki = "https://en.wikipedia.org/wiki/Comparison_between_Ido_and_Novial"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
Try = Extractor(wiki)
a = Try.get_Document()
All = Try.getAllWikitable(soup=a)
soup = Try.getAllParentsWikitable(tableslist=All)[0]


tables = Try.getAllParentsWikitable(tableslist=All)
conv = Convertor(tables)
sortie = conv.allTablesTo2D()
print(sortie)
