
import os
import codecs
import re
class Serializer():

    def __init__(self, list_value, url, index ):
        self.list_value = list_value
        self.url = url
        self.index = index

    def getUrl(self) :
        return self.url

    def getListValue(self):
        return self.list_value

    def assertPath(path) :
        your_string = re.sub(r'[\\*?:"<>|]',"",path)
        return your_string == path

    def serialize(self, path = "./output/html"):

        if self.assertPath == False:
            raise "Path Error"

        page=os.path.split(self.url)[1]
        f = codecs.open('{}/{}-{}.csv'.format(path, page, self.index), \
            'w',encoding='utf-8')
        for i in self.list_value:
            try :
                rowStr=';'.join(i)
            except :
                raise 'Double Table Error'
            rowStr=rowStr.replace('\n','')

            rowStr=rowStr
            f.write(rowStr+'\n')
        f.close()
