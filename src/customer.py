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
        sum = self.current_order.sum
        if self.is_contacted == True:
            self.has_take_order = True
            self.set_final_price(sum)
            self.print_order()
        else:
            print("Hat keine Bestellung bei uns gemacht.")

    def set_final_price(self, sum):
        self.need_to_pay = sum

    def print_order(self):
        # druckt Bestellung aus
        tuple = self.current_order.product_data
        print("#########################################################")
        print(f"# Bestellung von {self.company_name}".ljust(55), '#')
        print(f"# Bestellnr {self.current_order.order_ID}".ljust(55), '#')
        print(f"# ----------------------------------------------------- #")
        print(f"# Datum: 'getTime()'".ljust(55), '#')
        print(f"# Rechnungsadresse: {self.strasse},{self.plz},{self.ort}".ljust(55), '#')
        print(f"# Lieferadresse: {self.strasse},{self.plz},{self.ort}".ljust(55), '#')
        print(f"# ".ljust(55), '#')
        print("# Brotsorte,Menge,Einzelpreis".replace(",","    "), "Netto".rjust(19), '#')
        for e in tuple:
            print(f"# {e[0]}".ljust(14), f"{e[2]}".ljust(8), "{0:0.2f}".format(e[1]).ljust(14), "{0:16.2f}".format(e[3]), '#')
        print(f"# ".ljust(55), '#')
        print("# Gesamtpreis(netto): {0:33.2f}".format(self.need_to_pay), '#')
        print(f"# Name des Verkäufers: Simple Bakery".ljust(55), '#')
        print(f"# Liefertermin: 'heute oder morgen'".ljust(55), '#')
        print("#########################################################\n")

    def pay_bill_take_bread(self, boxes : Box_Stack):
        # Kunde zahlt die Rechnung
        if self.got_bill == True:
            
            # Brötchen in unsere Reserve wird weniger
            self.boxes_of_breads = boxes
            payment = self.need_to_pay
            return payment

    def __remove_current_order(self):
        self.current_order = None
    
    def print_bill(self):
        # Rechnung wird erstellt und gedruckt
        tuple = self.current_order.product_data
        if self.has_take_order:
            Customer.__billCounter += 1
            bill_id = str(Customer.__billCounter)
            self.bill_list.update({bill_id:self.current_order})
            self.__remove_current_order()
            self.got_bill = True
            print("#########################################################")
            print(f"# Rechnungsnummer: {Customer.__billCounter}".ljust(55), '#')
            print(f"# Datum: 'getTime()'".ljust(55), '#')
            print(f"# Bestellnr.: {self.current_order.order_ID}".ljust(55), '#')
            #print(f"# Kunden-ID:".ljust(47), '#')
            print(f"# Rechnungsadresse: {self.strasse},{self.plz},{self.ort}".ljust(55), '#')
            print(f"# Lieferadresse: {self.strasse},{self.plz},{self.ort}".ljust(55), '#')
            print(f"# ".ljust(55), '#')
            print("# Brotsorte,Menge,Einzelpreis".replace(",","    "), "Netto".rjust(19), '#')
            for e in tuple:
                print(f"# {e[0]}".ljust(14), f"{e[2]}".ljust(8), "{0:0.2f}".format(e[1]).ljust(14), "{0:16.2f}".format(e[3]), '#')
            print(f"# ".ljust(55), '#')
            print("# Gesamtpreis(netto): {0:33.2f}".format(self.need_to_pay), '#')
            print(f"# Steuern: - ".ljust(55), '#')
            print(f"# Zahlungsbedingung: Überweisung".ljust(55), '#')
            print(f"# Name des Verkäufers: Simple Bakery".ljust(55), '#')
            print("#########################################################\n")
        else: print("Existiert nicht")

    def reset_to_default_state(): pass


# rechnungen = {'RN001': [Brotsorte, Menge, Einzelpreis, Gesamtpreis]}



''' Erweiterungen:
- Klasse Bestellung/Warenkorb
- Kunde hat eine Liste an Bestellungen bei uns
- neue Bestellungen hinzufügen durch bestell_list.append(bestellung)
- Bestellnr und Rechnungsnr

- Steuern berücksichtigen
- Kunden zufällig generieren durch customer_info.txt und Dateizugriff
- Extra Klasse für das Kunden-Zufallsgenerator

erledigt:
- Kunde erhält (Kasten mit) Brote: breads.append(bread)
- Brote aus unsere Reserve wird weniger
- Kunden Nachfrage zufällig generieren
- einfache Berechnung des Gesamtpreises
- Funktion für das Kalkulieren von Einzel- und Gesamtpreis bei Bestellungen mit verschiedenen Brotsorten
'''
