import TemplateHTML.Grid.Grid
import TemplateHTML.Visitor.Visitor

from abc import ABC, abstractmethod

class Balise(ABC):
    def __init__(self, tag, from_table):
        self.span_row = 1
        self.span_col = 1
        self.depth = 0
        self.tag = tag
        self.from_table = from_table
        self.children = list()

    @abstractmethod
    def accept(visitor):
        pass

    def getInfo():
        pass

    def nextRowPos():
        return 1

    def isFinal():
        return not self.children

    # def init():

    def initGrid():
        self.initGrid(self.isFinal())

    def initGrid(is_final):
        if is_final:
            self.grid = Grid()
            self.grid.
