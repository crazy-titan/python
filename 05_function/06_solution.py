# lambda functions are the functions having no name and used once for some small tasks
# most of the time lambda functions are used in frameworks 



# def cube(num):
#     return num ** 3

# print(cube(3))
# ABOVE METHOD IS USED WHEN WE WANT TO CALL THE FUNCTION AGAIN N AGAIN

# see how LAMBDA is written

cube = lambda num: num ** 3  # num is a parameter and lambda function is stored in another variable 'cube'
print(cube(3))    # will output as 27

# we can't use this again n again anywhere, its just used and done here only
# we can't write something like
# another_cube = cube(3) not possible in lambda