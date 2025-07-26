# we will now see the concept of strings in python.
# we will still use the python shell for understanding concepts.
# we will now use the print syntax mainly for practising it more.
# sting support unicode character, UTF-8,UTF-16 

# >>> Tea = "hello world"
# >>> Tea
# 'hello world'
# >>> print(Tea)
# hello world
# >>> print(Tea[0])          // accessing 1st index of 'Tea' string.
# h
# >>> print(Tea[-1])         // accessing the first index of 'Tea' if we start index from end.
# d


# Slicing of string:

# >>> Number
# '0123456789'
# >>> print(Number[:])     // all index from start to end.
# 0123456789
# >>> print(Number[0:7])   // start from 0 and end at index 6 , becz last value in exclusive.
# 0123456

# >>> Number
# '0123456789'
# >>> print(Number[0:7:2]) // here the '2' tells that skip 1 element every time till index 6, becz 7 exclusive
# 0246
# >>> print(Number[0:7:3]) // here the '3' tells that skip 2 element every time till index 6, becz 7 exclusive
# 036

# >>> Tea = "Hello World"
# >>> Tea
# 'Hello World'
# >>> print(Tea.lower())      // methods require parenthesis , lower()
# hello world
# >>> print(Tea.upper())     // methods require parenthesis , upper()
# HELLO WORLD

# sometimes user give extra space, so how to handle that data?

# >>> Tea = "   Masala Tea     "
# >>> Tea
# '   Masala Tea     '
# >>> print(Tea.strip())         // use strip method to remove extra space 
# Masala Tea

# can we make a list from a string? Yes we can by using the 'split' method.

# >>> Tea = "Masala Tea, Ginger Tea, Lemon Tea"
# >>> Tea
# 'Masala Tea, Ginger Tea, Lemon Tea'
# >>> print(Tea.split())      // to make into list
# ['Masala', 'Tea,', 'Ginger', 'Tea,', 'Lemon', 'Tea'] // default.. make using seperation of space.
# >>> print(Tea.split(", "))    // mentioning the technique what to consider while making list.
# ['Masala Tea', 'Ginger Tea', 'Lemon Tea']


# some more function or method of strings.

# >>> Tea = "Lemon Tea"
# >>> Tea
# 'Lemon Tea'
# >>> print(Tea.replace("Lemon","Masala"))   // to replace lemon with masala
# Masala Tea
# >>> Tea
# 'Lemon Tea'    // string are immutable hence, reference is same.

# 'Find' a character or a string inside a string.

# >>> print(Tea.find("Tea"))     // above example give me the starting location of 'Tea'
# 6

# 'Count' a character or a string inside a string.

# >>> Tea = "Masala tea tea tea tea"
# >>> Tea
# 'Masala tea tea tea tea'
# >>> print(Tea.count("tea"))    // to count the number of times certain value occur in a string.
# 4

# how to replace the variable inside another variable....

# >>> Tea_type = "Masala Tea"
# >>> orders = 2
# >>> Order_now = "You have selected {}, having {} in numbers"     // {} are called placeholder.
# >>> Order_now
# 'You have selected {}, having {} in numbers'
# >>> print(Order_now.format(Tea_type,orders))  // to mentioned the placeholder values respectively.
# You have selected Masala Tea, having 2 in numbers   // final output.

# can we make the string from a list as we have seen the string can be converted to list.?
# yes we can make it happen also. using "".join syntax

# >>> list = ["lemon","ginger","masala"]
# >>> list
# ['lemon', 'ginger', 'masala']
# >>> print("".join(list))     // default
# lemongingermasala
# >>> print(",".join(list))    // seperate using comma ','
# lemon,ginger,masala 
# >>> print(" ".join(list))    // seperate using 'space'
# lemon ginger masala


# some issue with the path of windows , see the example 
# let's suppose i have some special or werid character in my string , and i want to treat as it is
# no change then how to do that?

# >>> tea = "Masala\nTea"
# >>> tea
# 'Masala\nTea'
# >>> print(tea)
# Masala
# Tea
# As we can see above while executing the print syntax 'Masala' and 'Tea' both come in different line.
# in these situation we use raw method , represented using small 'r'
#
# >>> print(r"Masala\nTea")   // now you can see the output will come as it is no change.
# Masala\nTea

# One more senerio where you want to write some quotes 
# intro = "Hey, i am "Electrica" student."
#  File "<python-input-59>", line 1
#     intro = "Hey, i am "Electrica" student."

# to make this happen we use backslash '\'character in front of the character that we want to make it ignore while printing.
# intro = "Hey, i am \"Electrica\" student."
# >>> intro
# 'Hey, i am "Electrica" student.'
# These are very usefull in case of path location in case of windows.