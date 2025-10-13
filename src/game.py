'''
Hier wird die Spielmechanik implementiert
'''
from baker import Baker
from oven import Oven
from bread import Bread
from box import Box
from box import Box_Stack
from customer import Customer
from bread import Brezel
from bread import Kaese_Brezel
from dough import Dough
import random
random.seed()

customer_list : Customer = []
customer_list.append(Customer("Brot To Go", "brot.to.go@mail.de", '01765201845', 'Mustermannstr. 17', '80335', 'München'))
customer_list.append(Customer("Bäckerei Brot & Herz", "brotuherz.bk@mail.de", '01765201846', 'Max-Mustermannstr. 3', '80331', 'München'))
customer_list.append(Customer("Oma Emmy's Bäckerei", "oma.emmyBaekerei@mail.de", '01765201844', 'Max-Mustermann-Platz 8', '80331', 'München'))

class Game:
    
                
    def __init__(self):
        pass

    def play(self):
        baker = Baker('Max','Mustermann', 3800)
        

        print("1. Erstmal backen \n2. Nach Kunden suchen")
        wahl = input()
        match wahl:
            case '1':
                
                baker.setNewDough()
                baker.mix_ingredients()
                baker.knead_dough()
                many_dough = baker.devide_and_form() # Liste an Teigklumpen

                breads_not_baked = baker.form_bread(many_dough)
                oven = Oven()
                baked_bread = baker.put_bread_into_oven(breads_not_baked, oven)
                #box = Box()
                boxes = Box_Stack()
                baker.take_bread_into_boxes(baked_bread, boxes, 5)
                
            case '2':
                
                popup = random.randint(0,2)
                #nachfrage_klein = [True, False] # True=0, False=1
                true_false = random.randint(0,1)
                boxes = Box_Stack()
                customer_list[popup].generate_demand(true_false)
                customer_list[popup].to_be_contacted(True)

                warenkorb = []
                menge = []
                pos_preis = []
                #choseBread
                demand = customer_list[popup].bread_demand
                choice_1 = random.randint(0,demand)
                choice_2 = demand - choice_1
                if choice_2 == 0:
                    brezel = Brezel(Dough())
                    warenkorb.append([brezel.name,brezel.s_price])
                    menge.append(choice_1)
                elif choice_1 == 0:
                    kaese_b = Kaese_Brezel(Dough())
                    warenkorb.append([kaese_b.name,kaese_b.s_price])
                    menge.append(choice_2)
                else:
                    brezel = Brezel(Dough())
                    kaese_b = Kaese_Brezel(Dough())
                    warenkorb.append([brezel.name,brezel.s_price])
                    warenkorb.append([kaese_b.name,kaese_b.s_price])
                    menge.append(choice_1)
                    menge.append(choice_2)

                
                customer_list[popup].take_order(warenkorb,menge,pos_preis) # 3 param
                customer_list[popup].print_bill()
                verdient = customer_list[popup].pay_bill_take_bread(boxes)
                print(verdient)

game = Game()
game.play()