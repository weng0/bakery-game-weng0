'''
Python Klasse für den Bäcker
'''

class Baker:
    def __init__(self, first_name, surname, salary):
        self.first_name = first_name
        self.surname = surname
        self.salary = salary

    def mix_ingredients(self, something):
        ''' Alle Zutaten für das Brot werden in einer Masse vermischt.
        Eingabeparametern sind die Zutaten
        Rückgabewert ist der Teig
        '''
        pass

    def knead_dough(self, something):
        '''Durch das Methode Kneten wird der Teig, der als Eingabeparameter übergeben wird, bearbeitet.'''
        pass

    def form_dough(self, something):
        '''Durch dieser Methode wird der Teig in kleineren Teile zerteilt und geformt. Der Teig wird als Parameter übergeben.'''
        pass