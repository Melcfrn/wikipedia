

class Convertor():
    def __init__(self, tables):
        self.rowspans = list()
        self.tables = tables
        self.colcount = 0

    def toStringTable(self, table) :
        """
        """

    def toStringTables(self, tables) :
        """
        """

    def tableTo2d(self, table):
        self.rowspans = list()
        self.colcount = 0
        rows = self.getRows(table)

        for r, row in enumerate(rows):
            self.getRowspans(row, r, table)

        new_table = [[None] * self.colcount for row in rows]

    def colCounter(self, colcount):
        self.colcount = max(colcount, sum(int(c.get('colspan', 1)) or 1 \
            for c in cells[:-1]) + len(cells[-1:]) + len(self.rowspans))
        return self.colcount

    def getRows(self, table):
        rows = table.find_all('tr')
        return rows

    def getRowspans(self, row, indice, table):
        cells = row.find_all(['td', 'th'], recursive=False)
        self.colcount = self.colCounter(self.colcount)
        rows = self.getRows(table)
        self.rowspans += [int(c.get('rowspan', 1)) or len(rows) - indice for c in cells]
        self.rowspans = [s - 1 for s in self.rowspans if s > 1]
        return self.rowspans
