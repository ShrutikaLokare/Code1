#constructor is one method which automatically called when you create object for any class

class Calculator():   #defining class
    sum = 40
    def __init__(self):       #default constructor
        print("I am called automatically when object is called")

    def add(self):     #function inside the class is called method
        print("addition")

obj = Calculator()    #giving a variable to class  to store the value

print(obj.sum)
obj.add()