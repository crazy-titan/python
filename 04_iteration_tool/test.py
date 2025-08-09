# we will now learn the internal working of loops
# about iter tools(iter(),__next__,next()) and iter objects(list,files)

# The working starts with the iteration tools , which goes to iter objects and __next__ will do 
# the iteration work on it.

# let's see the python shell results to understand what i am saying,

# iters.py is the file in the directory you can see


# >>> f = open('iters.py')
# >>> f.readline()
# 'print("TITAN")\n'
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'user_name = "ELECTRICAL"\n'
# >>> f.readline()
# 'print(user_name)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''

# open is used to open the file and then storing the reference in 'f' variable
# readline() is used as the index value printing in array

# you can imagine that file's code is stored in database in a form of lines. Because there are lines 
# inside the files and at last you can see output is empty string which denotes that lines are not there
# all done.


# >>> f = open('iters.py')
# >>> f.__next__()
# 'print("TITAN")\n'
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# 'user_name = "ELECTRICAL"\n'
# >>> f.__next__()
# 'print(user_name)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<python-input-13>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration

# This is the other method by using the __next__ which works same as readline(). But the readline()
# handled the error in best way and output as empty string whereas using __next__ at last it make
# stop iteration exception.


# Now lets take an example of list iter object

# >>> myList = [1,2,3,4]
# >>> I = iter(myList)
# >>> I
# <list_iterator object at 0x102809a20> // always point the same position never change
# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<python-input-22>", line 1, in <module>
#     I.__next__()
#     ~~~~~~~~~~^^
# StopIteration


# >>> iter(myList) is myList
# False
# >>> f = open('iters.py')
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__()
# True

# file automatically do this
# iter(f)
# where as list don't do that automatically. Hence answer were false and true respectively



# >>>
# D = {'a': 1, 'b':2}
# for key in D.keys():
# print (key)
# a
# b
# >> I = iter (D)
# >>> I
# ‹dict_keyiterator object at 0x102f81990>
# >>> next（I）
# 'a'
# >>>
# next （I）
# 'b'
# >>> next（I）
# Traceback (most recent call last):
# File "«stdin›", line 1, in ‹module›
# stopIteration exception


# are the range is also iter?
# >>> R
# range(0, 6)
# >>> I = iter(R)
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> 
# >>> next(I)
# 5
# >>> next(I)
# Traceback (most recent call last):
#   File "<python-input-17>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration


# use 'for' to print the file lines

# >>> f = open('iters.py')
# >>> for line in open('iters.py'):
# ...     print(line,end = '')
# ...     
# print("TITAN")
# import time
# user_name = "ELECTRICAL"
# print(user_name)>>> 

# use 'while' loop to print the line of file
# >>> while True:
# ...     lines = f.readline()
# ...     if not lines: break   // this will give true if line is not there, and false if line is there
# ...     print(lines)      // else part , it will print lines
# ...     
# print("TITAN")

# import time

# user_name = "ELECTRICAL"

# concept of NOT
# >>>
# >>>
# test = "hitesh"
# if not test:
# print ("chai")
# ...

# >>> test = ""
# >>> if not test:
# print("chai")
# ...
# ... chai


# these are the basis and understanding the internal working of loops.