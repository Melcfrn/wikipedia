import pandas as pd

test = pd.read_html("https://en.wikipedia.org/wiki/Comparison_between_Argentine_provinces_and_countries_by_GDP_(PPP)_per_capita", attrs={"class": "wikitable"})
print(test[0])
