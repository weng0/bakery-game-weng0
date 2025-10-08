'''
Kunden
'''

class Customer:
    def __int__(self, name, email, tel, strasse, plz, ort):
        self.company_name = name
        self.email = email
        self.tel = tel
        self.strasse = strasse
        self.plz = plz
        self.ort = ort

    def to_be_contacted(self): pass
        # wird von uns kontaktiert

    def generate_demand(self): pass
        # die Menge an Bedarf des Kunden wird zufällig generiert

    def take_order(self): pass
        # Kunde nimmt die Bestellung auf

    def pay_the_bill(self): pass
        # Kunde zahlt die Rechnung

    def print_order_bill(self): pass
        # Rechnung wird erstellt und gedruckt