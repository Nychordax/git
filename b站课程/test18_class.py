class Calculator:
    name = 'Good calculator'
    price = 18
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
calcul = Calculator()
calcul.add(5,6)