oxford = {
    "key":"value",
    "gift": "something willingly given to someone appriciate",
    "this": "a keyword in c++",
    "youtube": "a video sharing platform",
    "instagram": "a picture sharing platform",
    "mylist":"[1,3,45]"
    #[1,3,45] :"mylist" cant do this
}

# print( oxford.items())
    #print(a,b) #here a store key and b store value

for a,b in oxford.items():
       print(a,":",b)
# notes
print(oxford.keys()) 
print(oxford.values())
oxford.update({"debu":"baby" , "mylist":[56,8]}) # can add and can change
print(oxford)  

for key in oxford.keys() :
          print(key)

print(oxford.get("instagram"))    


                # more on docpython.org