class EmployeeForDev:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    

    def printobj(self):
        print(f"the name is {self.name}")
        print(f"the marks is {self.marks}")

D = EmployeeForDev("DEBJIT",98)
R = EmployeeForDev("ROHAN",99)
D.printobj()
R.printobj()
print(D.name)

