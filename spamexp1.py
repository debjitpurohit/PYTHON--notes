spamwords =["buy now","subscribe now","click this"]

email= input("enter your email :")

if( "buy now" in email or "subscribe now" in email or "click this" in email):
    spam =True  
else:
    spam = False
print("spam is ",spam)        