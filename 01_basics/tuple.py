# we will not discuss too much about tuple, only thing you need to know that is a type of list but 
# its immutable in nature.

# let's go on python shell to know about tuples.

# making of tuple
# >>> my_tuple = ("Black","Green","Yellow")
# >>> my_tuple
# ('Black', 'Green', 'Yellow')

# Access the tuple
# >>> my_tuple[1]
# 'Green'

# slicing and diecing are same to same as list


# we can't assign the value, once its created
# >>> my_tuple[1] = "okok"
# Traceback (most recent call last):
#   File "<python-input-10>", line 1, in <module>
#     my_tuple[1] = "okok"
#     ~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment


# adding of tuple you can also use this in list
# >>> your_tuple = ("Tea","Leaves","color")
# >>> all_tuple = your_tuple + my_tuple
# >>> all_tuple
# ('Tea', 'Leaves', 'color', 'Black', 'Green', 'Yellow')

# find the length of tuple
# >>> yo_tuple = ("Tea","maze","Tea")
# >>> yo_tuple
# ('Tea', 'maze', 'Tea')
# >>> len(yo_tuple)
# 3

# we can also ask question here just like dictionary and list
# >>> if "Tea" in yo_tuple:
# ...     print("yes i got you")
# ...     
# yes i got you

# we can also use the count method to count certain value
# >>> yo_tuple.count("Tea")
# 2

# check the type 
# >>> type(yo_tuple)
# <class 'tuple'>

# we can also assign a tuple to another
# >>> (check,find,search) = yo_tuple
# >>> check
# 'Tea'
# >>> find
# 'maze'
# >>> 