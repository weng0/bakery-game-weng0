'''
Kunden
'''
from box import Box_Stack
from bread import Bread
import random
random.seed()




class Customer:
    def __init__(self, name, email, tel, strasse, plz, ort):
        self.company_name = name
        self.email = email
        self.tel = tel
        self.strasse = strasse
        self.plz = plz
        self.ort = ort
        self.bread_demand = 0
        self.is_contacted : bool = False
        self.has_take_order : bool = False
        self.got_bill : bool = False
        self.need_to_pay = 0
        self.boxes_of_breads = None
        self.bill_list = []

    def to_be_contacted(self, is_contacted) -> bool:
        # wird von uns kontaktiert
        self.is_contacted = is_contacted

    def generate_demand(self, demand_small):
        # die Menge an Bedarf des Kunden wird zufällig generiert
        #self.bread_demand = 0
        if demand_small:
            self.bread_demand = random.randint(5,20)
        else: # demand_big
            self.bread_demand = random.randint(21,40)
        print("##########################################")
        print(f"# Nachfrage bei {self.company_name}".ljust(40),'#')
        print("# -------------------------------------- #")
        print(f"# Wir benötigen {self.bread_demand} Brötchen!".ljust(40),'#')
        print(f"# Bitte nehme Kontakt mit uns auf.".ljust(40), '#')
        print(f"# Adresse:".ljust(40), '#')
        print(f"# {self.strasse}, {self.plz}, {self.ort}".ljust(40), '#')
        print("# Kontakt:".ljust(40), '#')
        print(f"# Telefon {self.tel}".ljust(40), '#')
        print(f"# E-Mail {self.email}".ljust(40), '#')
        print("##########################################\n")
        return self.bread_demand

    def take_order(self):
        # Kunde nimmt die Bestellung auf
        if self.is_contacted == True:
            self.has_take_order = True
        else:
            print("Hat keine Bestellung bei uns gemacht.")

    def set_final_price(self, single_price):
        self.need_to_pay = self.bread_demand * single_price

    def print_order(self):
        # druckt Bestellung aus
        print("##########################################")
        print(f"# Bestellung von {self.company_name}".ljust(40), '#')
        print(f"#--------------------------------#")
        print(f"# Kaufdatum: 'getTime()'".ljust(40), '#')
        print(f"# Liefertermin: 'heute oder morgen'".ljust(40), '#')
        print(f"# Beschreibung der Bestellung: 'welcher Brotsorte und Menge'".ljust(40), '#')
        print(f"# Preis der Bestellung: {self.need_to_pay}".ljust(40), '#')
        print(f"# Lieferadresse: {self.strasse},{self.plz},{self.ort}".ljust(40), '#')
        print(f"# Name des Verkäufers: Simple Bakery".ljust(40), '#')
        print(f"# Rechnungsadresse:".ljust(40), '#')
        print("##########################################\n")

    def pay_bill_take_bread(self, boxes : Box_Stack):
        # Kunde zahlt die Rechnung
        if self.got_bill == True:
            
            # Brötchen in unsere Reserve wird weniger
            self.boxes_of_breads = boxes
            payment = self.need_to_pay
            return payment
        
    def print_bill(self):
        # Rechnung wird erstellt und gedruckt
        if self.has_take_order:
            self.got_bill = True
            print("##########################################")
            print(f"# Datum der Rechnung: 'getTime()'".ljust(40), '#')
            print(f"# Rechnungsnummer:".ljust(40), '#')
            print(f"# Nummer der Bestellung:".ljust(40), '#')
            print(f"# Beschreibung der Bestellung:".ljust(40), '#')
            print(f"# Preis jedes bestellten Artikels:".ljust(40), '#')
            print(f"# Name des Verkäufers: Simple Bakery".ljust(40), '#')
            print(f"# Rechnungsadresse: - ".ljust(40), '#')
            print(f"# Fälliger Gesamtbetrag: {self.need_to_pay}".ljust(40), '#')
            print(f"# Steuern: - ".ljust(40), '#')
            print(f"# Zahlungsbedingung: Überweisung".ljust(40), '#')
            print("##########################################")
        else: print("Existiert nicht")

    def reset_to_default_state(): pass


# customer_1 = Customer("Oma Emmy's Bäckerei", "oma.emmyBaekerei@mail.de", '01765201844', 'Max-Mustermann-Platz 8', '80331', 'München')
# customer_1.generate_demand(True)
# customer_1.to_be_contacted(True)
# customer_1.take_order()
# customer_1.print_order_bill()
# verdient = customer_1.pay_bill_take_bread()
# print(verdient)

# customer_2 : Customer
# customer_3 : Customer
# customer_4 : Customer

customer_list = []
customer_list.append(Customer("Brot To Go", "brot.to.go@mail.de", '01765201845', 'Mustermannstr. 17', '80335', 'München'))
customer_list.append(Customer("Bäckerei Brot & Herz", "brotuherz.bk@mail.de", '01765201846', 'Max-Mustermannstr. 3', '80331', 'München'))
customer_list.append(Customer("Oma Emmy's Bäckerei", "oma.emmyBaekerei@mail.de", '01765201844', 'Max-Mustermann-Platz 8', '80331', 'München'))

'Kunden zufällig generieren'
popup = random.randint(0,2)
nachfrage_klein = [True, False] # True=0, False=1
true_false = random.randint(0,1)
boxes = Box_Stack()
customer_list[popup].generate_demand(true_false)
customer_list[popup].to_be_contacted(True)
customer_list[popup].take_order()
customer_list[popup].print_bill()
customer_list[popup].set_final_price(1.20)
verdient = customer_list[popup].pay_bill_take_bread(boxes)
print(verdient)


''' Erweiterungen:
- Klasse Bestellung/Warenkorb
- Kunde hat eine Liste an Bestellungen bei uns
- neue Bestellungen hinzufügen durch bestell_list.append(bestellung)
- Bestellungen/Rechnungen abhacken

- komplexere Funktion für das Kalkulieren von Einzel- und Gesamtpreis bei Bestellungen mit verschiedenen Brotsorten
- Steuern berücksichtigen
- Kunden zufällig generieren durch customer_info.txt und Dateizugriff
- Extra Klasse für das Kunden Zufallsgenerator

erledigt:
- Kunde erhält (Kasten mit) Brote: breads.append(bread)
- Brote aus unsere Reserve wird weniger
- Kunden Nachfrage zufällig generieren
- einfache Berechnung des Gesamtpreises
'''
