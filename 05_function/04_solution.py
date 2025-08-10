# we have to make a program that gives area and perimeter as output

# import math
# def circle_stats(radius):
#     return math.pi * radius ** 2   # termination occur when 'return' is there
#     print('hi') # this will not execute becasue function terminate at 'return'

# # print() here we can see we just able to print one value that is area pir^2 

# how to handle more better?
import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area,perimeter    # we can return like this because two values are mentioned there

# how to print that values?
# simply hold in another variable(2 in number as per def)

a,c = circle_stats(5)  # because circle_stats give two values
print("Area:",a,"Perimeter:",c)   # solution will come in high precision
print("Area:",round(a,2),"Perimeter:",round(c,2))   # solution will come in low precision (2 digits)

# assignment is to make it low precision