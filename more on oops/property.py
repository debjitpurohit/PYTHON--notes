class Employee:
    a =2 #class attributes
    b=3
    c=4
    @classmethod
    def setAttribute(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c
    @property 
    def length (self):
        return self.a

emp =  Employee()
emp.setAttribute(105,502,205)
print(emp.length)
