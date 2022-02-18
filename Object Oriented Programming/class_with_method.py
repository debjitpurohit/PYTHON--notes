class EmployeeForDev:
    name = "debjit"
    marks = 34
    center ="delhi"
# self is the parameter use krle tobei class and object er information asbe
    def printobj(self):
        print(f"your name is {self.name} ")
        print(f"your marks is {self.marks} ")
        print(f"your center is {self.center} ")
    @staticmethod   #--> this method does not require any self parameter bcz this method does not use any object
    def greet():
        print("Good Day Debjit")    

debu = EmployeeForDev()
print(debu.name)
print(debu.marks)
print(debu.center)
debu.printobj()
EmployeeForDev.printobj(debu)
debu.greets()
