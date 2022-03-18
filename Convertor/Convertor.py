from bs4 import BeautifulSoup

class Convertor():
    def __init__(self, tables):
        self.rowspans = list()
        self.tables = tables
        self.colcount = 0
        self.span_offset = 0
        self.mapping_rowspans = dict()

    def tableTo2d(self, table):
        self.rowspans = list()
        self.colcount = 0
        rows = self.getRows(table)

        for r, row in enumerate(rows):
            self.getRowspans(row, r, table)

        new_table = [[None] * self.colcount for row in rows]

        self.mapping_rowspans = dict()
        for row, row_elem in enumerate(rows):
            self.span_offset = 0
            for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
                new_table = self.fillTable(row, row_elem, col, cell, table, new_table)
            self.mapping_rowspans = {c: s - 1 for c, s in self.mapping_rowspans.items() if s > 1}
        return new_table

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

    def fillTable(self, indice_row, row_elem, indice_col, cell, old_table, new_table):
        indice_col += self.span_offset
        while self.mapping_rowspans = dict().get(col, 0):
            span_offset += 1
            indice_col += 1
        rows = self.getRows(old_table)
        rowspan = self.mapping_rowspans[indice_col] = int(cell.get('rowspan', 1)) or len(rows) - indice_row
        self.colcount = self.colCounter(self.colcount)
        colspan = int(cell.get('colspan', 1)) or self.colcount - indice_col
        # next column is offset by the colspan
        self.span_offset += colspan - 1
        tableinc = cell.find("table",{"class":"wikitable"})
        if tableinc is not None:
            value = self.tableTo2d(cell)
        else :
            value = cell.get_text()
        for drow, dcol in product(range(rowspan), range(colspan)):
            try:
                if value != None :
                    new_table[row + drow][col + dcol] = value
                else :
                    new_table[row + drow][col + dcol] = " "
                self.mapping_rowspans[col + dcol] = rowspan
            except IndexError:
                # rowspan or colspan outside the confines of the table
                pass
        return new_table
