#                 loops
#whie loops 
'''a = 0
while(a<=100): #the block keeps executing until the condition is true
    print (a)
    a +=1'''

#quickquiz 1
'''a =1
while(a<=50):
     print(a)
     a=a+1'''

#quickquiz 2
'''a = [1,2,3,4,5,"bananna"]
i=0
while(i<len(a)):
     print(a[i])
     i=i+1
'''

#for loops
for i in range(34):  #range(n) 
       print(i)# print 0 to (n-1)....

for i in range(10,34):  #range(a,n) 
       print(i)# print a to (n-1)....

for i in range(10,34,2):  # step-size =2 .....i+=2
       print(i)

# for loop to print list  


a = [1,2,3,4,5,"bananna"]
for item in a:
    print(item) 

#for loop with else
l=[1,7,8]
for item in l:
       print(item)
else:
       print("done")  #this is printed when the loop exhaustnormally(programm fisnished succesfully) {break thakle else print hbe nh}        


b =[1,2,3,4,5,6]


for item in b:
    print(item)
    if(item == 3):
        continue
    print("done thisiteration for",item)
else:
       print("we are inside else")    
print("we have finished this loop")    