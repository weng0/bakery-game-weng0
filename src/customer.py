'''
Kunden
'''
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
        self.pay = 0

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
        print("###############")
        print(f"# Nachfrage bei {self.company_name} #")
        print("#-----------------------#")
        print(f"# Wir benötigen {self.bread_demand} Brötchen! #")
        print(f"# Bitte nehme Kontakt mit uns auf. #")
        print(f"# Adresse:           #")
        print(f"# {self.strasse}, {self.plz}, {self.ort} #")
        print("# Kontakt:                 #")
        print(f"# Telefon {self.tel}     #")
        print(f"# E-Mail {self.email}    #")
        print("############### \n")
        return self.bread_demand

    def take_order(self):
        # Kunde nimmt die Bestellung auf
        if self.is_contacted == True:
            self.has_take_order = True
            # druckt Bestellung aus
            print(f"##########################")
            print(f"# Bestellung von {self.company_name} #")
            print(f"#--------------------------------#")
            print(f"# Kaufdatum: 'getTime()' #")
            print(f"# Liefertermin: 'heute oder morgen' #")
            print(f"# Beschreibung der Bestellung: 'welcher Brotsorte und Menge' #")
            print(f"# Preis der Bestellung:   #")
            print(f"# Lieferadresse: {self.strasse},{self.plz},{self.ort} #")
            print(f"# Name des Verkäufers: Simple Bakery #")
            print(f"# Rechnungsadresse:  #")
            print(f"##########################")
        else:
            print("Hat keine Bestellung bei uns gemacht.")

    def pay_bill_take_bread(self):
        # Kunde zahlt die Rechnung
        if self.got_bill == True:
            self.pay = 20.00
            payment = self.pay
            # Brötchen in unsere Reserve wird weniger
            return payment
        
    def print_order_bill(self):
        # Rechnung wird erstellt und gedruckt
        if self.has_take_order:
            self.got_bill = True
            print(f"################")
            print(f"# Datum der Rechnung: 'getTime()' #")
            print(f"# Rechnungsnummer:  #")
            print(f"# Nummer der Bestellung:  #")
            print(f"# Beschreibung der Bestellung: #")
            print(f"# Preis jedes bestellten Artikels: #")
            print(f"# Name des Verkäufers: Simple Bakery #")
            print(f"# Rechnungsadresse: - #")
            print(f"# Fälliger Gesamtbetrag: - #")
            print(f"# Steuern: - #")
            print(f"# Zahlungsbedingung: Überweisung #")
            print(f"################")
        else: print("Existiert nicht")


customer_1 = Customer("Oma Emmy's Bäckerei", "oma.emmyBaekerei@mail.de", '01765201844', 'Max-Mustermann-Platz 8', '80331', 'München')
customer_1.generate_demand(True)
customer_1.to_be_contacted(True)
customer_1.take_order()
customer_1.print_order_bill()
verdient = customer_1.pay_bill_take_bread()
print(verdient)

''' Erweiterungen:
- Klasse Bestellung/Warenkorb
- Kunde hat eine Liste an Bestellungen bei uns
- neue Bestellungen hinzufügen durch bestell_list.append(bestellung)
- Bestellungen/Rechnungen abhacken
- Steuern berücksichtigen
- Kunde erhält (Kasten mit) Brote: breads.append(bread)
- Brote aus unsere Reserve wird weniger
- Kunden zufällig generieren durch neue Klasse/Funktion Anzeige

'''