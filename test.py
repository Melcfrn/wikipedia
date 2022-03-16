import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


test = pd.read_html("https://en.wikipedia.org/wiki/Comparison_between_Argentine_provinces_and_countries_by_GDP_(PPP)_per_capita", attrs={"class": "wikitable"})
print(test[0])




HTML = ""
# Open the HTML in which you want to make changes
html = requests.get("https://en.wikipedia.org/wiki/Comparison_between_Argentine_provinces_and_countries_by_GDP_(PPP)_per_capita").text
  
# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')
  
# Give location where text is stored which you wish to alter
unordered_list = soup.find("table",{"class":"wikitable"})

print(unordered_list)