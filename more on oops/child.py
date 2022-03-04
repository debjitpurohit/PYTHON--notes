class Employee: #base class
    a=34


class programmer(Employee): #child class
    b=32
   

pr= programmer()
print(pr.a)
print(pr.b)

em= Employee() 
print(em.a)
#print(em.b)#because employee have only a

