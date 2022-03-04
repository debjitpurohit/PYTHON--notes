#dunda methods
class Dunda:
    def __init__(self,a,name):
        self.a=a
        self.name=name

    def __add__(self,obj):
        return self.a+obj.a    

    def __str__(self) -> str:
        return str(self.name) 

    def __len__(self):
        return self.a

a=Dunda(10,"DEBJIT")
b=Dunda(20,"ROHAN") 


print(a,b)
print(a+b)
print(len(a))
print(len(b))