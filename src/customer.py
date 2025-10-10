'''
Kunden
'''
from box import Box_Stack
from bread import Bread
from order import Order
import random
random.seed()




class Customer:
    __billCounter : int = 137
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
        self.bill_list = {}
        self.current_order = None

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

    def take_order(self, bread_type, quantity, empty_lst):
        # Kunde nimmt die Bestellung auf
        self.current_order = Order()
        self.current_order.zip_data(bread_type, quantity, empty_lst)
        if self.is_contacted == True:
            self.has_take_order = True
            self.set_final_price(1.20)
            self.print_order()
        else:
            print("Hat keine Bestellung bei uns gemacht.")

    def set_final_price(self, single_price):
        self.need_to_pay = self.bread_demand * single_price

    def print_order(self):
        # druckt Bestellung aus
        tuple = self.current_order.product_data
        print("#################################################")
        print(f"# Bestellung von {self.company_name}".ljust(47), '#')
        print(f"# Bestellnr iterieren()".ljust(47), '#')
        print(f"# --------------------------------------------- #")
        print(f"# Datum: 'getTime()'".ljust(47), '#')
        print(f"# Rechnungsadresse: {self.strasse},{self.plz},{self.ort}".ljust(47), '#')
        print(f"# Lieferadresse: {self.strasse},{self.plz},{self.ort}".ljust(47), '#')
        print("# ID  Brotsorte    Menge  Einzelpreis  Netto".ljust(47), '#')
        for e in tuple:
            print(f"# 01 {e[0]}   {e[2]}  {e[1]}  {e[3]}", '#')
        print(f"#    ", '#')
        print(f"# Gesamtpreis(netto): {self.need_to_pay}".ljust(47), '#')
        print(f"# Name des Verkäufers: Simple Bakery".ljust(47), '#')
        print(f"# Liefertermin: 'heute oder morgen'".ljust(47), '#')
        print("#################################################\n")

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
            bill_id = str(Customer.__billCounter + 1)
            self.bill_list.update({bill_id:Order()})
            self.got_bill = True
            print("##########################################")
            print(f"# Rechnungsnummer: {Customer.__billCounter}".ljust(47), '#')
            print(f"# Datum: 'getTime()'".ljust(47), '#')
            print(f"# Bestellnr.:".ljust(47), '#')
            print(f"# Kunden-ID:".ljust(47), '#')
            print(f"# Rechnungsadresse: {self.strasse},{self.plz},{self.ort}".ljust(47), '#')
            print(f"# Lieferadresse: {self.strasse},{self.plz},{self.ort}".ljust(47), '#')
            print("# ID  Brotsorte    Menge  Einzelpreis  Netto".ljust(47), '#')
            print(f"# 01  Brot          {self.bread_demand}    1.20         {self.need_to_pay}".ljust(47), '#')
            print(f"# ".ljust(47), '#')
            print(f"# Gesamtpreis(netto): {self.need_to_pay}".ljust(47), '#')
            print(f"# Steuern: - ".ljust(40), '#')
            print(f"# Zahlungsbedingung: Überweisung".ljust(40), '#')
            print(f"# Name des Verkäufers: Simple Bakery".ljust(47), '#')
            print("##########################################")
        else: print("Existiert nicht")

    def reset_to_default_state(): pass


# rechnungen = {'RN001': [Brotsorte, Menge, Einzelpreis, Gesamtpreis]}


''' Erweiterungen:
- Klasse Bestellung/Warenkorb
- Kunde hat eine Liste an Bestellungen bei uns
- neue Bestellungen hinzufügen durch bestell_list.append(bestellung)
- Bestellnr und Rechnungsnr

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
