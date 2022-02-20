import math
class calculator:
    def __init__(self,number):
        self.number = number

    def square(self):
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number

    def squareRoot(self): #squareroot means Borgomool
        return math.sqrt(self.number)

d = calculator(2)
print(d.square())
print(d.cube())
print(d.squareRoot())

# we can use debjit insted of self
import math
class calculator:
    def __init__(debjit,number):
        debjit.number = number

    def square(debjit):
        return debjit.number * debjit.number
    
    def cube(debjit):
        return debjit.number * debjit.number * debjit.number

    def squareRoot(debjit): #squareroot means Borgomool
        return math.sqrt(debjit.number)

d = calculator(2)
print(d.square())
print(d.cube())
print(d.squareRoot())