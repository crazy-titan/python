username = "HotTea"   # global variable
 
def func1():    # scope defined
    # username = "Tea"   # local variable inside the scope # comment out this line to see output
    print(username)   # function is printing the local variable

print(username) # printing the global variable

func1()

# output will be HotTea and HotTea
# because there is no local variable for the defined functions hence, it will take the value of
# global variables.