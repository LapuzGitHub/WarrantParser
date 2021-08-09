
from enum import Enum, auto
from datetime import datetime


class WarrantFeature(Enum):
    ISIN = 0
    product = auto()
    underlying = auto()
    strike = auto()
    maturity = auto()
    delta = auto()
    bid = auto()
    ask = auto()
    pctChange = auto()
    leverage = auto()
    issuer = auto()


class Warrant:
    
    def __init__(self, dataString):

        self.ISIN = None
        self.isCall = None
        self.underlying = None
        self.strike = None
        self.maturity = None
        self.delta = None
        self.bid = None
        self.ask = None
        self.pctChange = None
        self.leverage = None
        self.issuer = None
        self.underlyingSpot = None
        self.quotity = None
        self.quotityBid = None
        self.quotityAsk = None

        endIndex = dataString.find('  ')
        indexFeature = 0

        while endIndex>=0:
        
            currentFeature = dataString[0:endIndex]
            self.set_feature(indexFeature, currentFeature)

            dataString = dataString[endIndex:].lstrip()
            endIndex = dataString.find('  ')
            indexFeature+=1


    def __str__(self):
 
        return f"{self.maturity.strftime('%Y-%m-%d')}\t{self.strike}\t{self.underlyingSpot}\t{self.isCall}\t{self.ISIN}\t{self.underlying}\t{self.pctChange}\t{self.leverage}\t{self.delta}\t{self.bid}\t{self.ask}\t{self.quotity}\t{self.quotityBid}\t{self.quotityAsk}\t{self.issuer}"


    def quoted(self):

        return self.bid != None or self.ask != None


    def set_feature(self, indexFeature, currentFeature):

        try:

            warrantFeature = WarrantFeature(indexFeature)
            if warrantFeature == WarrantFeature.ISIN:
                self.ISIN = currentFeature
            elif warrantFeature == WarrantFeature.product:
                self.isCall = (currentFeature == 'Warrants Call')
            elif warrantFeature == WarrantFeature.underlying:
                self.underlying = currentFeature
            elif warrantFeature == WarrantFeature.strike:
                self.strike = float(currentFeature.replace(' ', ''))
            elif warrantFeature == WarrantFeature.maturity:
                self.maturity = datetime.strptime(currentFeature, '%d/%m/%y')
            elif warrantFeature == WarrantFeature.delta:
                self.delta = round(float(currentFeature.rstrip('%'))/100., 2)
            elif warrantFeature == WarrantFeature.bid:
                self.bid = float(currentFeature)
            elif warrantFeature == WarrantFeature.ask:
                self.ask = float(currentFeature)
            elif warrantFeature == WarrantFeature.pctChange:
                self.pctChange = currentFeature
            elif warrantFeature == WarrantFeature.leverage:
                self.leverage = float(currentFeature)
                if self.leverage == 0.: self.leverage = None
            elif warrantFeature == WarrantFeature.issuer:
                self.issuer = str(currentFeature).title()
           
        except:

            pass
