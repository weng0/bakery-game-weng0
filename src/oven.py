'''
Klasse Ofen fürs Brotbacken
'''
from bread import Bread

class Oven:
    def __init__(self):
        self.temperature = None
        self.timer = 0
        self.bread_list = [] # Bitte korrigieren: Übergabeparameter soll eine Liste/Array an ungebackenen Brote sein

    def setTemperature(self, temperature):
        '''Temperatur festlegen'''
        self.temperature = temperature

    def setTimer(self, timer):
        '''Zeit zum Backen festlegen'''
        self.timer = timer