a =[1,2,3,4,5,6]


for item in a:
    print(item)
    if(item == 3):
        break
print("we have finished this loop")

b =[1,2,3,4,5,6]


for item in b:
    print(item)
    if(item == 3):
        continue
    print("done thisiteration for",item)
print("we have finished this loop")    