'''Bestellung
'''

class Order:
    __idCounter : int = 123
    def __init__(self): # take out
        # self.bread_dict = None
        # self.quantity = None
        self.sum = 0
        self.product_data = None # setProduct()
        Order.__idCounter += 1
        self.order_ID = Order.__idCounter
    
    def zip_data(self,bread_type,quantity, pos_price):# Brotsorte ist ein Dict
        sum = 0
        bread_lst = []
        einzel_preis = []
        if len(bread_type) == len(quantity):
            for index in range(len(quantity)):
                price = bread_type[index][1] * quantity[index]
                sum += price
                bread_lst.append(bread_type[index][0])
                einzel_preis.append(bread_type[index][1])
                pos_price.append(price)
        data_kombi_2 = zip(bread_lst,einzel_preis,quantity, pos_price)
        self.product_data = data_kombi_2
        self.sum = sum
        return data_kombi_2

    # def setProduct(self):
    #     self.product_data.update({})

