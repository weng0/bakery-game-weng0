'''Bestellung
'''

class Order:
    __idCounter : int = 123
    def __init__(self):
        self.sum = 0
        self.product_data = None
        Order.__idCounter += 1
        self.order_ID = Order.__idCounter
    
    def zip_data(self,bread_type,quantity, pos_price):
        sum = 0
        bread_lst = []
        single_price : float = []
        if len(bread_type) == len(quantity):
            for index in range(len(quantity)):
                price = bread_type[index][1] * quantity[index]
                sum += price
                bread_lst.append(bread_type[index][0])
                single_price.append(bread_type[index][1])
                pos_price.append(price)
        product_data = list(zip(bread_lst,single_price,quantity, pos_price)) # Lösung zum Problem, dass der Inhalt im zip() nicht ausgegeben wird
        self.product_data = product_data
        self.sum = sum
        return product_data