class Calculator:
    def __init__(self,name,price,hight=18,width=10,weight=5):
        self.name = name
        self.price = price
        self.hight = hight
        self.width = width
        self.weight = weight
    def add(self,x,y):
        print(self,x,y)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        result = x * y
        print(result)
    def divide(self,x,y):
        result = x / y
        print(result)


c = Calculator('bad calculator',12)