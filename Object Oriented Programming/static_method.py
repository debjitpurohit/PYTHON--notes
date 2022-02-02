class EmployeeForDev:
    name = "debjit"


    @staticmethod
    def greet():
        print(f"Good Day {EmployeeForDev.name}") 

    @staticmethod
    def greet2():
        print("Good Day baby") 


debu = EmployeeForDev()
debu.greet()
debu.greet2()