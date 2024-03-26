#Classes - 2 types of variables
# class variable - inside class and value does not change, always constant
# instance variable - inside constructor and can be changed
# constructor keyword __init__


class Calculator():                #defining class
    sum = 40                       #class variable
    def __init__(self, a, b):  #instance variable
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is called")

    def add(self):     #function inside the class is called method
        print("addition")

    def summation(self):
        return self.firstnumber + self.secondnumber + self.sum

obj = Calculator(5,5)    #assigning value to a and b

print(obj.summation())

obj1 = Calculator(10, 10)    #assigning value to a and b

print(obj1.summation())

