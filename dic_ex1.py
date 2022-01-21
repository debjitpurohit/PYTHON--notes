oxford = {
    "lakdi":"wood",
    "kurshi":"chair",
    "chaku":"knife"

}
key2 = input("enter the key \n")


if(oxford.get(key2)==None) :
    print("value is not in the oxford dictionary")
else:    
    print("the value corresponding to the key is" ,
oxford.get(key2))

print(type(key2))
print(type(oxford))