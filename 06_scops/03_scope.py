# lets investigate more about the scopes

toy = 101 # global variable

def addF(TOY_Destroy):
    total_toy = toy - TOY_Destroy
    return total_toy

# as we are returning the value, than store it somewhere
 
final = addF(1)   # storing 101 - 1 in final is better approach
print(final)     # print 100 


# here you can see toy is coming from global variable 
# and TOY_Destroy is the local variable
