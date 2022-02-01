with open("don.txt", "r") as f:
    text =f.read()

text2 = text.replace("donkey", "monkey")   

with open("don.txt" , "w") as f:
    f.write(text2)



