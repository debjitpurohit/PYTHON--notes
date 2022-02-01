'''factorial(5)=1*2*3*4*5
 thats like ...factorioal(n)=1*n-3*n-2*n-1*n
factorial(0)=1 
 factorial(1)=1
factorial(n)=n*n-1*n-2*n-3*n-4........*3*2*1
factorial(n)=n*(n-1*n-2*n-3*n-4*.....)
==factorial(n)=n*fctorial(n-1)''' 

def factorial(n):
    #base condition...nahole infinite e chole jabe 0!,,,-1!,,-2! ....kre kre infinte hye jabe 
     if(n==0 or n==1):
         return 1
     else:  
        a = int(n*factorial(n-1))
        return a
b =factorial(10)
print(b) 


#sum(8)=1+2+3+4+5+6+7+8
#sum(n)= n+sum(n-1)

def sum(n):
    if (n==1):
        return 1
    else:
        return n+sum(n-1)
a = sum(10)
print(a)  

def printPattern(n):
    for i in range(n):
         print("*"*(n-i))
a = printPattern(4)
print(a)