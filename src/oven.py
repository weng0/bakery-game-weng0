'''
Klasse Ofen fürs Brotbacken
'''
class Oven:
    def __init__(self, temperature, timer, dough):
        self.temperature = temperature
        self.timer = timer
        self.dough = dough # Bitte korrigieren: Übergabeparameter soll eine Liste/Array an ungebackenen Brote sein

    def setTemperature(self, temperature):
        '''Temperatur festlegen'''
        self.temperature = temperature

    def setTimer(self, timer):
        '''Zeit zum Backen festlegen'''
        self.timer = timer