'''
Brot
'''
from dough import Dough


class Bread:
    # Brot besteht ursprünglich aus Teig
    # Ein Brot hat zwei Zustände: 1) ungebacken=False und 2) gebacken=True
    def __init__(self,dough : Dough, baked=False):
        self.baked = baked
        self.dough = dough
        self.s_price = 1.20
        self.sort = 'standard'

    # Diese Funktion setzt den Zustand des Brotes auf gebacken
    def setBaked(self): 
        self.baked = True