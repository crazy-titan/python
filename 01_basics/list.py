# we will now see the concept and details about the list in python.

# List concepts are similar to the strings that we have discussed so far, and we know that list is
# mutable.

# we are using the python shell again to learn the concept.

# >>> tea_varieties = ["lemon","green","ginger","white"]     // initialisation of list
# >>> tea_varieties
# ['lemon', 'green', 'ginger', 'white']
# >>> print(tea_varieties)
# ['lemon', 'green', 'ginger', 'white']
# >>> tea_varieties[1]                       // accessing the list elements
# 'green' 
# >>> tea_varieties[1:3]               // slicing of list
# ['green', 'ginger']

# >>> tea_varieties[1] = "Yellow"       // changing the value in reference
# >>> tea_varieties
# ['lemon', 'Yellow', 'ginger', 'white']   // list is mutable

# >>> tea_varieties[1:1]      // start and not include it , wow feature for getting empty value
# []
# >>> tea_varieties[1:1] = "orange"    // analyse the output first 
# >>> tea_varieties
# ['lemon', 'o', 'r', 'a', 'n', 'g', 'e', 'Yellow', 'ginger', 'white']   // we can see that 'orange' is taking as array hence,
# its letter gets outputed one by one like the element of an array.


# >>> tea_varieties = ["lemon","green","ginger","white"]
# >>> tea_varieties[1:1] = ["orange"]   // passing as an array as whole
# >>> tea_varieties
# ['lemon', 'orange', 'green', 'ginger', 'white']  // you can see that it inject same as it is on index 1

# one more example same to same
# >>> tea_varieties[1:1] = ["orange","orange"]
# >>> tea_varieties
# ['lemon', 'orange', 'orange', 'green', 'ginger', 'white']
# >>> tea_varieties[1:2]
# ['orange']
# >>> tea_varieties[1:3]
# ['orange', 'orange']
# >>> tea_varieties[1:3] = []
# >>> tea_varieties
# ['lemon', 'green', 'ginger', 'white']


# append function to add an element at the end of the list
# >>> tea_varieties = ["lemon","green","ginger","white"]
# >>> tea_varieties.append("Yellow")
# >>> tea_varieties
# ['lemon', 'green', 'ginger', 'white', 'Yellow']

# pop() function to remove the last element from the list --> it will give you the value that is gone.
# >>> tea_varieties.pop()
# 'Yellow'

# we also have remove function to remove the elements from the list, it just remove without showing the value that's gone.
# >>> tea_varieties.remove("white")
# >>> tea_varieties
# ['lemon', 'green', 'ginger']

# we also have insert function to insert at particular indexes.
# >>> tea_varieties.insert(1,"insert")    // 1 is index and "insert" is the value
# >>> tea_varieties
# ['lemon', 'insert', 'green', 'ginger']   // as you can see all values get shifted right 

# we also have a copy function which basically make a reference which is copy of previous one and both are differnt pointing location.
# >>> tea_varieties_copy = tea_varieties.copy()
# >>> tea_varieties_copy.insert(1,"insert2")    // change the values in copy list
# >>> tea_varieties_copy
# ['lemon', 'insert2', 'insert', 'green', 'ginger']
# >>> tea_varieties        // original list
# ['lemon', 'insert', 'green', 'ginger']


# we also have list comprehension
# >>> tea_cups = [x**2 for x in range(10)]
# >>> tea_cups
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# list comprehension is the interesting method to make a list of my own without writing more.

# by default print function print the loops output values in next line (\n)
# >> for i in tea_cups:
# ...         print(i , end = "-")
# ...         
# 0-1-4-9-16-25-36-49-64-81->>>  that why pointer comes right now.