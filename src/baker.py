'''
Der Bäcker und alle seine Tätigkeiten
'''
from dough import Dough
from bread import Bread

class Baker:
    def __init__(self, first_name, surname, salary):
        self.first_name = first_name
        self.surname = surname
        self.salary = salary
        self.dough_0 = None
        self.dough_list = [] # Reserve
        self.bread_list = [] # Reserve

    def setNewDough(self):
        self.dough_0 = Dough()

    def mix_ingredients(self):
        ''' Alle Zutaten für das Brot werden in einer Masse vermischt.
        Die Funktion fordert solange nach einer Eingabe, bis man alle fehlende Zutaten eins nach dem anderen eingegeben hat.
        Rückgabewert ist der Teig.
        '''
        #self.setNewDough()
        while self.dough_0.isFinished() == False:
            print('Was wollen Sie hinzugeben?\n', '1.Wasser\n', '2.Mehl\n','3.Milch\n','4.Salz\n','5.Zucker\n', '6.Butter\n','7.Hefe\n')
            choice = input()
            match choice:
                case '1':
                    print('Bitte die korrekte Menge an Wasser eingießen.'+'\n')
                    inp = int(input())
                    self.dough_0.water = inp       
                case '2':
                    print('Bitte die korrekte Menge an Mehl eingeben.'+'\n')
                    inp = int(input())
                    self.dough_0.flour = inp                
                case '3':
                    print('Bitte die korrekte Menge an Milch eingeben.'+'\n')
                    inp = int(input())
                    self.dough_0.milk = inp                 
                case '4':
                    print('Bitte die korrekte Menge an Salz eingeben.'+'\n')
                    inp = int(input())
                    self.dough_0.salt = inp                 
                case '5':
                    print('Bitte die korrekte Menge an Zucker eingeben.'+'\n')
                    inp = int(input())
                    self.dough_0.sugar = inp 
                case '6':
                    print('Bitte die korrekte Menge an Butter eingeben.'+'\n')
                    inp = int(input())
                    self.dough_0.butter = inp 
                case '7':
                    print('Bitte die korrekte Menge an Hefe eingeben.'+'\n')
                    inp = int(input())
                    self.dough_0.yeast = inp
            self.dough_0.updateMass() # dadurch werden die Werte in ingredients überschrieben
        return self.dough_0

    def knead_dough(self):
        '''Teig wird geknetet. Setzt den Zustand auf 'Teig geknetet', in Form einer bool-Wert'''
        self.dough_0.kneaded = True

    def devide_and_form(self): # statt form_dough
        '''Durch dieser Methode wird der Teig in kleineren Stücke zerteilt und geformt.
        Rückgabewert: Liste an Teigklumpen'''
        # Dem dough_0 Masse wird solange ein Portion (90.55g) abgezogen bis von der dough_0 Masse nichts mehr übrig bleibt.
        # Danach wird self.dough_0 wieder auf None gesetzt
        # Ergebnis soll eine Liste an Teigklumpen sein
        one_mass = self.dough_0.mass
        one_portion = 90.55 # in Gramm, siehe Kommentar bei class Dough member variablen
        portions_float = one_mass // one_portion # berechnet Anzahl an Portionen
        portions = int(portions_float)
        rest = one_mass % one_portion # Der Rest, der nicht weiter geteilt werden kann

        for p in range(portions):
            one_mass = one_mass - one_portion
            self.dough_list.append(Dough(15, 50, 15.45, 0.5, 0.4, 5, 4.2)) # ein Portion wird erzeugt und in die Reserve abgelegt
            if p == portions: # Der kleinerer Rest wird in die letze Portion reingeknetet
                rest = rest + portions # ?% + 100%
                multiplier = (rest*100//one_portion)/100 # ungefähr 1.?%
                self.dough_list.append(Dough(15*multiplier, 50*multiplier, 15.45*multiplier, 0.5*multiplier, 0.4*multiplier, 5*multiplier, 4.2*multiplier))
        return self.dough_list
    
    def form_bread(self, dough_list : Dough):
        # Eingabeparameter: dough_list
        # Objekte aus dough_list werden eins nach dem anderen rausgenommen und den Objekten der Klasse Brot zugeordnet
        # Rückgabewert: Liste an ungebackenen Brote
        return self.bread_list

