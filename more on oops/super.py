class Parent: 
    a =8
    def __init__(self):
        print("Parent class")
class child1(Parent): 
    b =9 
    def __init__(self):
        super().__init__() #call constructor of parent class (parent is parent class of child 1)
        print("child1 class")  

class child2(child1): 
    c =12
    def __init__(self):
        super().__init__() #call constructor of   parent class(child1 is parent class of child 2)
        print("child2 class")

ch= child2()
print(ch.a)
print(ch.b)
print(ch.c)