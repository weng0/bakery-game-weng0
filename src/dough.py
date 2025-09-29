'''
Der Teig kommt zustande, wenn man alle benötigen Zutaten zusammen gemischt hat
'''
class Dough: # alle eingaben
    def __init__(self, water=None, flour=None, milk=None, salt=None, sugar=None, butter=None, yeast=None):
        self.water = water
        self.flour = flour
        self.milk = milk
        self.salt = salt
        self.sugar = sugar
        self.butter = butter
        self.yeast = yeast
        self.ingredients = {'Wasser':self.water, 'Mehl':self.flour, 'Milch': self.milk, 'Salz':self.salt, 'Zucker':self.sugar, 'Butter':self.butter, 'Hefe':self.yeast} # Das ist die Zutatenliste

    def updateMass(self): # Diese Funktion aktualisiert ingredients dictionary
        self.ingredients.update({'Wasser':self.water, 'Mehl':self.flour, 'Milk': self.milk, 'Salz':self.salt, 'Zucker':self.sugar, 'Butter':self.butter, 'Hefe':self.yeast})
        

    def dough_rise(self, time) -> bool:
        pass

    def isFinished(self) -> bool: # Fehler liegt bei ingredients dictionary, es muss stets aktualisiert werden
        # Diese Funktion geht solange durch die Zutatenliste, bis festgestellt wird, dass ein Zutat noch fehlt
        finished = True
        for i in self.ingredients:
            if self.ingredients[i] is None:
                print(f'Es fehlt noch {i}!')
                finished = False
                break
        return finished
