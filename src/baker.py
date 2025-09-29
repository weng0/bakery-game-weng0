'''
Der Bäcker und alle seine Tätigkeiten
'''
from dough import Dough

class Baker:
    def __init__(self, first_name, surname, salary):
        self.first_name = first_name
        self.surname = surname
        self.salary = salary
        self.dough_0 = None

    def setNewDough(self):
        self.dough_0 = Dough()

    def mix_ingredients(self):
        ''' Alle Zutaten für das Brot werden in einer Masse vermischt.
        Die Funktion fordert solange nach einer Eingabe, bis man alle fehlende Zutaten eins nach dem anderen eingegeben hat.
        Rückgabewert ist der Teig.
        '''
        #self.setNewDough()
        while self.dough_0.isFinished() == False:
            print('Was wollen Sie hinzugeben?\n', '1.Wasser\n', '2.Mehl\n')
            choice = input()
            match choice:
                case '1':
                    print('Bitte die korrekte Menge an Wasser eingießen.'+'\n')
                    inp = input()
                    self.dough_0.water = inp
                case '2':
                    print('Bitte die korrekte Menge an Mehl eingeben.'+'\n')
                    inp = input()
                    self.dough_0.flour = inp
                case '3':
                    print('Bitte die korrekte Menge an Milch eingeben.'+'\n')
                    inp = input()
                    self.dough_0.milk
                case '4':
                    print('Bitte die korrekte Menge an Salz eingeben.'+'\n')
                    inp = input()
                    self.dough_0.salt
                case '5':
                    print('Bitte die korrekte Menge an Zucker eingeben.'+'\n')
                    inp = input()
                    self.dough_0.sugar
                case '6':
                    print('Bitte die korrekte Menge an Butter eingeben.'+'\n')
                    inp = input()
                    self.dough_0.butter
                case '7':
                    print('Bitte die korrekte Menge an Hefe eingeben.'+'\n')
                    inp = input()
                    self.dough_0.yeast
            self.dough_0.updateMass() # dadurch werden die Werte in ingredients überschrieben
        return self.dough_0

    def knead_dough(self, something):
        '''Durch das Methode Kneten wird der Teig, der als Eingabeparameter übergeben wird, bearbeitet.'''
        pass

    def form_dough(self, something):
        '''Durch dieser Methode wird der Teig in kleineren Teile zerteilt und geformt. Der Teig wird als Parameter übergeben.'''
        pass

# baker = Baker('Max','Mustermann', 3800)
# baker.setNewDough()
# baker.mix_ingredients()