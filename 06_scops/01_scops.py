# Scope is represent by currly brackets but in python we will manage it using indentation

# outer or global variable can be access by scope functions or mentioned variables whereas 
# vice-versa is not true.


# function (){

# }
# this is the general representation of scope in programmig

# how to represent scope inside python?

username = "HotTea"   # global variable
 
def func1():    # scope defined
    username = "Tea"   # local variable inside the scope
    print(username)   # function is printing the local variable

print(username) # printing the global variable

# if we run this file nothing will be output other than 'HotTea'

# to investigate the working of the scope lets call the 'func1' that we just made