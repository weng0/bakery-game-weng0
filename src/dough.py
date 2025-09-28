'''
Der Teig kommt zustande, wenn man alle benötigen Zutaten zusammen gemischt hat
'''
class Dough:
    def __init__(self, water=None, flour=None, milk=None, salt=None, sugar=None, butter=None, yeast=None):
        self.water = water
        self.flour = flour
        self.milk = milk
        self.salt = salt
        self.sugar = sugar
        self.butter = butter
        self.yeast = yeast
        self.ingredients = {'Water':self.water, 'Flour':self.flour} # es fehlen noch die restlichen

    def dough_rise(self, time) -> bool:
        pass

    def isFinished(self) -> bool:
        finished = True
        for i in self.ingredients: # Solange durch die Zutatenliste gehen, bis geprüft wird, dass ein Zutat noch fehlt
            if self.ingredients[i] == None:
                print(f'Es fehlt noch {i}!')
                finished = False
                break
        return finished


teig = Dough(100, 300)

status = teig.isFinished()
print(status)

