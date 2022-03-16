import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


test = pd.read_html("https://en.wikipedia.org/wiki/Comparison_between_Argentine_provinces_and_countries_by_GDP_(PPP)_per_capita", attrs={"class": "wikitable"})
#print(test[0])




# Open the HTML in which you want to make changes
html = requests.get("https://en.wikipedia.org/wiki/Help:Table").text
  
# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')
  
# Give location where text is stored which you wish to alter
unordered_list = soup.find_all("table",{"class":"wikitable"})
parentl = []
for i in unordered_list : 
    parentl.append(i.parent("table"))



with  open("python.txt", "w", encoding="utf-8") as file:
    file.write(str(unordered_list))
    file.write("  \n   ")
    file.write("-----")
    file.write("  \n   ")
    file.write(str(parentl))
    file.close()