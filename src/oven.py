'''
Klasse Ofen fürs Brotbacken
'''
from bread import Bread
import time
import datetime

class Oven:
    def __init__(self):
        self.temperature = None
        self.total_seconds = 0
        self.bread_list = []

    def setTemperature(self, temperature):
        '''Temperatur festlegen'''
        self.temperature = temperature

    def countdown_timer(self, h, m, s):
        '''Zeit zum Backen festlegen'''
        self.total_seconds = h *3600 + m * 60 + s

        while self.total_seconds >0:
            timer = datetime.timedelta(seconds=self.total_seconds)
            time.sleep(1)
            self.total_seconds -= 1
        print("Bzzzt! Die Brote sind fertig!")