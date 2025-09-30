'''
Der Teig kommt zustande, wenn man alle benötigen Zutaten zusammen gemischt hat
'''
class Dough:
    # 1 Portion
    def __init__(self, water=None, flour=None, milk=None, salt=None, sugar=None, butter=None, yeast=None):
        self.water = water # 15ml = 15g
        self.flour = flour # 50g
        self.milk = milk # 1,03g/ml*15ml = 15.45g
        self.salt = salt # 1 Teelöffel is 5g, 0.1TL= 0,5g
        self.sugar = sugar #1 Teelöffel is 4g, 0.1TL=0,4g
        self.butter = butter # 5g
        self.yeast = yeast # 1 Würfel=42g , 0.1Würfel= 4.2g
        self.ingredients = {'Wasser':self.water, 'Mehl':self.flour, 'Milch': self.milk, 'Salz':self.salt, 'Zucker':self.sugar, 'Butter':self.butter, 'Hefe':self.yeast} # Das ist die Zutatenliste
        self.kneaded : bool = False
        self.mass : int = 0

    def updateMass(self): # Diese Funktion aktualisiert den Inhalt, die der Masse hinzugefügt wurden, und rechnet aus, wie schwer die akutelle Teigmasse ist
        self.ingredients.update({'Wasser':self.water, 'Mehl':self.flour, 'Milch': self.milk, 'Salz':self.salt, 'Zucker':self.sugar, 'Butter':self.butter, 'Hefe':self.yeast})
        mass = 0
        for i in self.ingredients:
            if i != None:
                mass = mass + self.ingredients[i]
        self.mass = mass
        
    def dough_rise(self, time) -> bool:
        pass

    def isFinished(self) -> bool: # Fehler liegt bei ingredients dictionary, es muss stets aktualisiert werden
        # Diese Funktion geht solange durch die Zutatenliste, bis festgestellt wird, dass ein Zutat noch fehlt
        finished = True
        for i in self.ingredients:
            if self.ingredients[i] == None:
                print(f'Es fehlt noch {i}!')
                finished = False
                break
        return finished
