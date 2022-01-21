 # set is a collection of non-repetative element and set is unindex(cant access element with in a set by index)index number diye kono element k set er moddhe thaka obostaii call krte parbo nh 
s1 = {1,2,2,3,4,5,"debu"}
#print(s1[3])



print(len(s1)) #hisab moto length 7 but dekhacche 6 bcz set in non repetative tai 2 ta k ekbar e dhorche
print(type(s1))

s1.remove(3)
print(s1)

s1.add("babu")
#s.add("debu") length not increased jehetu debu already set er mddhe ache
print(s1)

print(s1.pop())
print(s1)

#s.clear()
#print(s)

s2=s1.union({"sona","baby","manu"})
print(s2) # union mane duto set add hye jabe

s3= s2.intersection({"sona","baby","manu"})
print(s3)#intersection mane 

s4 = s1.intersection({4,122}) ## only 4 is common between s4 and s1
print(s4)

s5 = s1.intersection({10,13}) # nothing is common between s5 and s1
print(s5) # intersection become 0