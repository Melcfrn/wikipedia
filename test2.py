from itertools import product
from queue import Empty
from urllib import request
from bs4 import BeautifulSoup
from Extractor.Extractor import Extractor
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


def table_to_2d(table_tag):
    rowspans = []  # track pending rowspans
    rows = table_tag.find_all('tr')

    # first scan, see how many columns we need
    colcount = 0
    for r, row in enumerate(rows):
        cells = row.find_all(['td', 'th'], recursive=False)
        #print("+++,", cells, "---, ")
        #for cell in cells:
            #tableinc = cell.find("table",{"class":"wikitable"})
            #if len(tableinc)
        # count columns (including spanned).
        # add active rowspans from preceding rows
        # we *ignore* the colspan value on the last cell, to prevent
        # creating 'phantom' columns with no actual cells, only extended
        # colspans. This is achieved by hardcoding the last cell width as 1. 
        # a colspan of 0 means “fill until the end” but can really only apply
        # to the last cell; ignore it elsewhere. 
        colcount = max(
            colcount,
            sum(int(c.get('colspan', 1)) or 1 for c in cells[:-1]) + len(cells[-1:]) + len(rowspans))
        # update rowspan bookkeeping; 0 is a span to the bottom. 
        rowspans += [int(c.get('rowspan', 1)) or len(rows) - r for c in cells]
        rowspans = [s - 1 for s in rowspans if s > 1]

    # it doesn't matter if there are still rowspan numbers 'active'; no extra
    # rows to show in the table means the larger than 1 rowspan numbers in the
    # last table row are ignored.

    # build an empty matrix for all possible cells
    table = [[None] * colcount for row in rows]

    # fill matrix from row data
    rowspans = {}  # track pending rowspans, column number mapping to count
    for row, row_elem in enumerate(rows):
        span_offset = 0  # how many columns are skipped due to row and colspans 
        for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
            # adjust for preceding row and colspans
            print("+++,", cell, "---, ")
            col += span_offset
            while rowspans.get(col, 0):
                span_offset += 1
                col += 1

            # fill table data
            rowspan = rowspans[col] = int(cell.get('rowspan', 1)) or len(rows) - row
            colspan = int(cell.get('colspan', 1)) or colcount - col
            # next column is offset by the colspan
            span_offset += colspan - 1
            tableinc = cell.find("table",{"class":"wikitable"})
            if tableinc is not None:
                value = table_to_2d(cell)
            else :
                value = cell.get_text()
            for drow, dcol in product(range(rowspan), range(colspan)):
                try:
                    if value != None :
                        table[row + drow][col + dcol] = value
                    else :
                        table[row + drow][col + dcol] = " "
                    rowspans[col + dcol] = rowspan
                except IndexError:
                    # rowspan or colspan outside the confines of the table
                    pass

        # update rowspan bookkeeping
        rowspans = {c: s - 1 for c, s in rowspans.items() if s > 1}

    return table
j=0
for table in tables :
    data = table_to_2d(table)
    page=os.path.split(wiki)[1]
    f = codecs.open('table{}{}.csv'.format(j,page), 'w',encoding='utf-8')
    for i in data:
        for k in i : 
            if k is None :
                k = "   "
        print(i)
        rowStr=','.join(i)
        rowStr=rowStr.replace('\n','')
            #print(rowStr)
        rowStr=rowStr#.encode('unicode_escape')
        f.write(rowStr+'\n')      
    j+=1
    f.close()