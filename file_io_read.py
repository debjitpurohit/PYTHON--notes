f = open("this.txt", "r")
text = f.read()
print(text)
f.close()

f = open("this.txt", "r")
txt=f.read(6)
print(txt)
f.close()


# readline
f = open("this.txt", "r")
# txt2=f.readline()
# print(txt2)
# txt2=f.readline()
# print(txt2)
# txt2=f.readline()
# print(txt2)
text2 = f.readlines() # print as a list
print(text2)
f.close()


