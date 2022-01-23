num =int(input("enter your number \n"))

for i in range(2,num):
    if (num%i == 0):
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")