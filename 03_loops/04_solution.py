my_string = "Python"   # let's assume we have this string
reversed_string = ""   # take it as empty

# for i in my_string:
#     reversed_string = reversed_string + i # this will give you same result as you have in my_string
# print(reversed_string)
for i in my_string:
    reversed_string = i + reversed_string  # this will give you reverse result
print(reversed_string)

# the concept in 2nd approach is that i am adding the i value first where as in first method 
# i am adding the i value in end which is making the same sting again.
# thing like this you will become more good
