name = input("enter your name \n")
date = input("enter your date \n")

template = '''
Dear <|name|>,
You are selected
<|date|>
'''
print(template.replace("<|name|>" , name).replace("<|date|>",date))