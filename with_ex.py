with open ("poem.txt","r") as f :
    if ('twinkle' in f.read()):
        print("yes twinkle is present ")
    else:
        print("no twinkle is not present")    