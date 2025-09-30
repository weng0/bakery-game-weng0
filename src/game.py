'''
Hier wird die Spielmechanik implementiert
'''
from baker import Baker
from oven import Oven
from bread import Bread

class Game:
    def __init__(self):
        pass

    def play(self):
        baker = Baker('Max','Mustermann', 3800)
        baker.setNewDough()
        baker.mix_ingredients()
        baker.knead_dough()
        many_dough = baker.devide_and_form() # Liste an Teigklumpen
        
        print(baker.dough_list)
        print(len(baker.dough_list))
        print(baker.dough_list[10].ingredients)

        baker.form_bread(many_dough)

game = Game()
game.play()