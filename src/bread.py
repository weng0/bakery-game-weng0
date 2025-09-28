'''
Brot
'''
class Bread:
    # Ein Brot hat zwei Zustände:
    # ungebacken=False und gebacken=True
    def __init__(self,baked=False):
        self.baked = baked

    # Diese Funktion setzt den Zustand des Brotes auf gebacken
    def isBaked(self): 
        self.baked = True