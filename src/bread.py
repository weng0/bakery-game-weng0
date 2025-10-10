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
        self.s_price = 1.00
        self.name = 'standard'

    # Diese Funktion setzt den Zustand des Brotes auf gebacken
    def setBaked(self): 
        self.baked = True

class Brezel(Bread):
    def __init__(self, dough : Dough, baked=False):
        super().__init__(dough, baked)
        self.s_price = 1.30
        self.name = 'Brezel'
        self.laugen = True
        self.salz = True

class Kaese_Brezel(Bread):
    def __init__(self, dough : Dough, baked=False):
        super().__init__(dough, baked)
        self.s_price = 1.50
        self.name = 'Käsebrezel'
        self.laugen = True
        self.kaese = True

# class Laugenzopf(Bread):
#     pass
