# *args is used when you don't know how many parameters are coming form the input

# always use the print method to check what is actully coming as output from a particular function

# sum() is an inbuilt function in python which just add the elements or parameters

def sum_all(*args):
    return args

print(sum_all(1,2,4,8))  # will give tuple  (1, 2, 4, 8)

###

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,4,8))  # will give the sum = 15

###

def sum_all(*args):
    print(args)      # give tuple
    for i in args:
        print(i)     # give each element one by one
    return sum(args) # give sum of elements = 15

print(sum_all(1,2,4,8))  # print the value as = 15

###

def sum_all(*args):
    print(*args)      # give numbers like 1 2 4 8
    for i in args:
        print(i)     # give each element one by one
    return sum(args) # give sum of elements = 15

print(sum_all(1,2,4,8))  # print the value as = 15


### CAN WE USE SOMETHING DIFFERENT IN PLACE OF *ARGS?

def sum_all(*hello):
    return sum(hello)

print(sum_all(1,2,4,8))

# yess we can write like this but this is not a good and professional way to do ,
# always use 'args'