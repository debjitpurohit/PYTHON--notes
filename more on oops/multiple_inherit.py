class Parent1: #base class 1
    a =4
   
class Parent2: #base class 2
    b =6   
   
class child(Parent1,Parent2): #child class inherit from more then one parent class
    c =9
    

ch= child()
print(ch.a)
print(ch.b)
print(ch.c)