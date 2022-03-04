class Employee:
    a =2 #class attributes
    b=3
    c=4
    @classmethod
    def setAttribute(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c
        

emp =  Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)

emp.setAttribute(105,502,205)
print(Employee.a)
print(Employee.b)
print(Employee.c)