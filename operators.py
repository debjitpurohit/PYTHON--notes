# arithmatic operators

a3 = 45
b3 = 64


print("a3+b3=", a3+b3)
print("a3-b3=", a3-b3)
print("a3*b3=", a3*b3)
print("a3/b3=", a3/b3)

#modulus operator

number = int (input("enter the number: "))
print("reminder when the number devided by 2 is: ",number%2)

# assingment operator

c = 10   # = itself is an assingment opeartaor
_d = 6

print(c, _d)

c += 4     # += operator increase the value of c by 4 ( 10+4)
_d += 2    # += opearator increase the value of _d by 2(6+2)
print(c, _d)

c -= 2     # -= operator decrease the value of c by 4(14-2)
_d -= 1   # -= opearator decrease the value of _d by 2(8-1)
print(c, _d)

# comparrison operator

m = 6
n = 8

print( m == n )  
print( m <= n)
print( m < n)
print( m >= n)
print( m > n)
print( m != n) # true or false logic comes out

# logical operator
# in and operator both of the condition is true then true
# in or operator either of this condn is true then true printed

                        
print( m ==n and m>n)
print( m ==n and m<n)
print( m <n and m<n)   

print( m >n or m<n)
print(m==n or m>n) 
print( m>n or m<n)   
print( not(m>n))        
                        # not flase = true and not true = false
x = 56
y ="56"

print(x == y)

#     * operator

h = 4
print("the square of 4 is ", h*h)