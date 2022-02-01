import os
oldname= input("enter the name of the file \n")
newname = input("enter a new name \n ")

with open(oldname, "r") as f:
    text =f.read()

with open(newname, "w") as f:
       f.write(f"file is renamed by {newname}")

os.remove(oldname)