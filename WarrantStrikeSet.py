
from collections import OrderedDict

class WarrantStrikeSet:
    
    def __init__(self):

        self.warrantStrikeDictionary = {}


    def add(self, warrant):

        if not warrant.strike: return

        if warrant.strike not in self.warrantStrikeDictionary:
            self.warrantStrikeDictionary[warrant.strike] = []

        self.warrantStrikeDictionary[warrant.strike].append(warrant)


    def sort(self):

        self.warrantStrikeDictionary = OrderedDict(sorted(self.warrantStrikeDictionary.items()))


