#Inheritance is acquiring qualities of parent class

from parentclass import Calculator

class child(Calculator):
    num2 = 100

    def __init__(self):
        Calculator.__init__(self, 10, 10)

    def getCompleteData(self):
        return self.num2 + self.sum + self.summation()


obj = child()
print(obj)



