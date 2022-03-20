from Extractor.Extractor import Extractor
from Convertor.Convertor import Convertor
from Serializer.Serializer import Serializer

wiki = "https://en.wikipedia.org/wiki/Comparison_(grammar)"
# wiki = "https://en.wikipedia.org/wiki/Comparison_between_Ido_and_Novial"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
Try = Extractor(wiki)
a = Try.get_Document()
All = Try.getAllWikitable(soup=a)
soup = Try.getAllParentsWikitable(tableslist=All)[0]


tables = Try.getAllParentsWikitable(tableslist=All)
conv = Convertor(tables)
sortie_conv = conv.allTablesTo2D()
for i, table in enumerate(sortie_conv):
    serial = Serializer(table, wiki, i)
    serial.serialize()
