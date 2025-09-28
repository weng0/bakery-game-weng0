'''
Der Teig kommt zustande, wenn man alle benötigen Zutaten zusammen gemischt hat
'''
class Dough:
    def __init__(self, water, flour, milk, salt, sugar, butter, yeast):
        self.water = water
        self.flour = flour
        self.milk = milk
        self.salt = salt
        self.sugar = sugar
        self.butter = butter
        self.yeast = yeast

    def dough_rise(self, time) -> bool:
        pass