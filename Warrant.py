
from enum import Enum, auto
from datetime import datetime


class WarrantFeature(Enum):
    ISIN = 0
    Product = auto()
    Underlying = auto()
    ExercisePrice = auto()
    Maturity = auto()
    Delta = auto()
    Bid = auto()
    Ask = auto()
    PctChange = auto()
    Leverage = auto()
    Issuer = auto()


class Warrant:
    
    def __init__(self, dataString):

        self.ISIN = None
        self.IsCall = None
        self.Underlying = None
        self.ExercisePrice = None
        self.Maturity = None
        self.Delta = None
        self.Bid = None
        self.Ask = None
        self.PctChange = None
        self.Leverage = None
        self.Issuer = None
        self.UnderlyingSpot = None
        self.Quotity = None

        endIndex = dataString.find('  ')
        indexFeature = 0

        while endIndex>=0:
        
            currentFeature = dataString[0:endIndex]
            self.SetFeature(indexFeature, currentFeature)

            dataString = dataString[endIndex:].lstrip()
            endIndex = dataString.find('  ')
            indexFeature+=1


    def __str__(self):
 
        return f"{self.Maturity.strftime('%Y-%m-%d')}\t{self.ExercisePrice}\t{self.UnderlyingSpot}\t{self.IsCall}\t{self.ISIN}\t{self.Underlying}\t{self.PctChange}\t{self.Leverage}\t{self.Delta}\t{self.Bid}\t{self.Ask}\t{self.Quotity}\t{self.Issuer}"


    def SetFeature(self, indexFeature, currentFeature):

        try:

            warrantFeature = WarrantFeature(indexFeature)
            if warrantFeature == WarrantFeature.ISIN:
                self.ISIN = currentFeature
            elif warrantFeature == WarrantFeature.Product:
                self.IsCall = (currentFeature == 'Warrants Call')
            elif warrantFeature == WarrantFeature.Underlying:
                self.Underlying = currentFeature
            elif warrantFeature == WarrantFeature.ExercisePrice:
                self.ExercisePrice = float(currentFeature.replace(' ', ''))
            elif warrantFeature == WarrantFeature.Maturity:
                self.Maturity = datetime.strptime(currentFeature, '%d/%m/%y')
            elif warrantFeature == WarrantFeature.Delta:
                self.Delta = round(float(currentFeature.rstrip('%'))/100., 2)
            elif warrantFeature == WarrantFeature.Bid:
                self.Bid = float(currentFeature)
            elif warrantFeature == WarrantFeature.Ask:
                self.Ask = float(currentFeature)
            elif warrantFeature == WarrantFeature.PctChange:
                self.PctChange = currentFeature
            elif warrantFeature == WarrantFeature.Leverage:
                self.Leverage = float(currentFeature)
                if self.Leverage == 0.: self.Leverage = None
            elif warrantFeature == WarrantFeature.Issuer:
                self.Issuer = str(currentFeature).title()
           
        except:

            pass
