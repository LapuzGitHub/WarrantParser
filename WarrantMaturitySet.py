
from WarrantStrikeSet import WarrantStrikeSet
from collections import OrderedDict

class WarrantMaturitySet:
    
    def __init__(self):

        self.warrantMaturityDictionary = {}


    def add(self, warrant):

        if not warrant.maturity: return

        if warrant.maturity not in self.warrantMaturityDictionary:
            self.warrantMaturityDictionary[warrant.maturity] = WarrantStrikeSet()

        self.warrantMaturityDictionary[warrant.maturity].add(warrant)


    def sort(self):

        self.warrantMaturityDictionary = OrderedDict(sorted(self.warrantMaturityDictionary.items()))
        for warrantStrikeSet in self.warrantMaturityDictionary.values():
            warrantStrikeSet.sort()