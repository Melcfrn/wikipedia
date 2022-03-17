import TemplateHTML.Balise.Balise
import TemplateHTML.Balise.table
import TemplateHTML.Balise.Void

import numpy as np

class Grid():

    def __init__(self, final_balise=None):
        self.grid = list()
        self.from_table = True
        if final_balise:
            self.grid.append(final_balise)
            self.from_table = final_balise.getFromTable()

    def span(span_row, span_col):
        self.squareUp()
        init_size = self.getRowSize()

        for j in range(span_row-1):
            for i in range(init_size):
                row_copy = self.getRow(i)
                self.grid.append(row_copy)

        init_size = self.getRowSize()

        for i in range(init_size)
