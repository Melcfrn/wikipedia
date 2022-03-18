from queue import Empty
from urllib import request
from bs4 import BeautifulSoup
from Extractor.Extractor import Extractor
import os
import codecs
import numpy as np
wiki = "outuput_Comparison_between_Ido_and_Novial.html"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
Try = Extractor(wiki)
a = Try.get_Document()
All = Try.getAllWikitable(soup=a)
soup = Try.getAllParentsWikitable(tableslist=All)[0]
 

tables = Try.getAllParentsWikitable(tableslist=All)

# show tables
for table in tables:
    print("###############")
    print(table.text[:100])

    for tn in range(len(tables)):
        table=tables[tn]

    # preinit list of lists
        rows=table.findAll("tr")
        row_lengths=[len(r.findAll(['th','td'])) for r in rows]
        ncols=max(row_lengths)
        nrows=len(rows)
        data=[]
        for i in range(nrows):
            rowD=[]
            for j in range(ncols):
                rowD.append('')
            data.append(rowD)

    # process html
        for i in range(len(rows)):

            row=rows[i]
            rowD=[]
            cells = row.findAll(["td","th"])
         
            for j in range(len(cells)):
                cell=cells[j]
                print(cell.text)

            #lots of cells span cols and rows so lets deal with that
                cspan=int(cell.get('colspan',1))
                rspan=int(cell.get('rowspan',1))
                print(np.size(data))
                for l in range(cspan):
                    #data[i][count] = cell.text  
                    for k in range(rspan):
                        #print(l)
                        count=0
                        #while data[i+k][l+j+count] is not Empty : 
                        #    count+=1
                        data[i+k][l+j+count] += cell.text
                        
                        
                      

            #data.append(rowD)

    # write data out
    
        page=os.path.split(wiki)[1]
        fname='output_{}_t{}.csv'.format(page,tn)
        f = codecs.open(fname, 'w',encoding='utf-8')
        for i in range(nrows):
            rowStr=','.join(data[i])
            rowStr=rowStr.replace('\n','')
            #print(rowStr)
            rowStr=rowStr#.encode('unicode_escape')
            f.write(rowStr+'\n')      
        
        
    f.close()