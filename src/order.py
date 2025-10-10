'''Bestellung
'''
brotsorte = {'Breze':1.20, 'Croissant':2.45}
menge = [10, 20]
class Order:
    __idCounter : int = 123
    def __init__(self): # take out
        # self.bread_dict = None
        # self.quantity = None
        self.price = 0
        self.product_data = None # setProduct()
        self.order_ID = Order.__idCounter
    


    # def setProduct(self):
    #     self.product_data.update({})