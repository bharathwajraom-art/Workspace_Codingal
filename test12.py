class Computer:
    def __init__(self):
        self.max_price=900
    def sell(self):
        print("selling price:{}".format(self.max_price))
    def setmaxprice(self,price):
        self.max_price=price
c=Computer()
c.sell()
c.max_price=1000
c.sell()
c.setmaxprice(1000)
c.sell()
