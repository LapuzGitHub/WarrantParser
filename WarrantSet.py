
from WarrantMaturitySet import WarrantMaturitySet

class WarrantSet:
    
    def __init__(self):

        self.warrantList = []
        self.warrantMaturitySet = WarrantMaturitySet()


    def add(self, warrant):
        
        self.warrantList.append(warrant)
        self.warrantMaturitySet.add(warrant)


    def sort(self):

        self.warrantMaturitySet.sort()
