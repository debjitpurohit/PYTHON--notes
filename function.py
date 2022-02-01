# a function can be reused by developer anytime anywhere
def func1():  
    #these 4 line within func1() call as function defenation
    print("hello harry")
    print("you are good")
    print("i am third")
    print("i am fourth")
#--> this all are call function call
func1()   
func1()  
func1()   
func1()   
func1()   


def user():
    c = input("enter your employee name : \n ")
    print("Good Day",c)

user()

'''function is 2 type  ...built in and user defined...
builtin are [ len(), range(), print()]
user defined are [ func1(), user()]'''