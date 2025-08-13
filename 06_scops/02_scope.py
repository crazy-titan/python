username = "HotTea"   # global variable
 
def func1():    # scope defined
    username = "Tea"   # local variable inside the scope
    print(username)   # function is printing the local variable

print(username) # printing the global variable

func1() # calling the function

# now we will get output first as "HotTea" and second output as "Tea"
# this is because func1() will print local variable value whereas the outside print will print 
# the global value.
