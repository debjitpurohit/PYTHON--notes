# when a child class becomes a parent for another child class
class Parent: #base class 1
    a =8
class child1(Parent): #child class inherit from  parent class
    b =9   

class child2(child1): #child2(PARENT OF child1) class inherit from child1 class
    c =12

ch= child2()
print(ch.a)
print(ch.b)
print(ch.c)