
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
        
        allStrikes = set()
        for warrantMaturity in self.warrantMaturityDictionary:
            currentKeys = self.warrantMaturityDictionary[warrantMaturity].getKeys()
            for currentKey in currentKeys:
                allStrikes.add(currentKey)
  
        globalWarrantDictionary = {}
        for warrantMaturity in self.warrantMaturityDictionary:
            currentStrikeDictionary = self.warrantMaturityDictionary[warrantMaturity].getDict()
            for strike in allStrikes:
                if strike in currentStrikeDictionary:
                    currentWarrants = ""
                    for warrant in currentStrikeDictionary[strike]:
                        if currentWarrants != "": currentWarrants += "\n"
                        currentWarrants += str(warrant)
                    currentStrikeDictionary[strike] = currentWarrants
                else:
                    currentStrikeDictionary[strike] = ""
            globalWarrantDictionary[warrantMaturity] = OrderedDict(sorted(currentStrikeDictionary.items()))
        return globalWarrantDictionary
