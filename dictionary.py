# dictionary is a collectoion of  key value pairs
# dictionary er motoi onek vaule thakbe jokhon mon jabe jta khusi amra print korate pari
oxford = {
    "key":"value",
    "gift": "something willingly given to someone appriciate",
    "this": "a keyword in c++",
    "youtube": "a video sharing platform",
    "instagram": "a picture sharing platform",
    "mylist":[1,3,45]
    #[1,3,45] :"mylist" cant do this
}


print(oxford)
print(oxford["this"])
print(oxford.get('instagram')) 
print(type(oxford)) #dictionary class