'''
Hier wird die Spielmechanik implementiert
'''
from baker import Baker
from oven import Oven
from bread import Bread
from box import Box

class Game:
    def __init__(self):
        pass

    def play(self):
        baker = Baker('Max','Mustermann', 3800)
        baker.setNewDough()
        baker.mix_ingredients()
        baker.knead_dough()
        many_dough = baker.devide_and_form() # Liste an Teigklumpen

        breads_not_baked = baker.form_bread(many_dough)
        oven = Oven()
        baked_bread = baker.put_bread_into_oven(breads_not_baked, oven)
        box = Box()
        baker.take_bread_into_boxes(baked_bread, box)

game = Game()
game.play()