# we will now see the concepts of dictionary, its similar like list with little bit more info to handle.
# again we will use the python shell to learn the concepts.

# Dictionary start with the keyword 'dict' or just use the curly brackets {}

# >>> tea_shop = {"Masala" : "haldi","Lemon":"red","Ginger":"Fresh"}
# >>> tea_shop
# {'Masala': 'haldi', 'Lemon': 'red', 'Ginger': 'Fresh'}

# Accessing the dictionary.
# >>> tea_shop["Masala"]       // always give the key to get the values
# 'haldi'

# The difference in list and dictionary is that you give the values in list and keys are index which are present by default
# whereas in dictionary,you have to set the key and value both and there is no any particular sequence for accessing
# you can access any random.

# you can update or change the values by accessing its key.
# >>> tea_shop["Masala"] = "value"
# >>> tea_shop
# {'Masala': 'value', 'Lemon': 'red', 'Ginger': 'Fresh'}

# you can also access the value using get('key') method here you don't have to use the '[]' just use key in ""
# >>> tea_shop.get("Ginger")
# 'Fresh'

# what will happen if i write wrong key value in get and [] commands, let's check.
# >>> tea_shop.get("Gingerr")  // nothing as output no response

# >>> tea_shop["Gingerr"]
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     tea_shop["Gingerr"]                          // we will got response that something is wrong
#     ~~~~~~~~^^^^^^^^^^^
# KeyError: 'Gingerr'

# how to use the pop("key") command in dictionary
# >>> tea_shop.pop("Ginger")         // here we have to mention the key that want to remove.
# 'Fresh'    
# >>> tea_shop
# {'Masala': 'value', 'Lemon': 'red'}   // as u can see Ginger key and its values gets removed

# how to remove the last added key and value for the dictionary?
# >>> tea_shop.popitem()    // remove the last key and value which you have added to the dictionary.
# ('Lemon', 'red')         
# >>> tea_shop
# {'Masala': 'value'}     // final left dictionary as you can see

# copy() command is same to same like the list which make a copy or reference and then both are treated as different.

# how to add the keys and value to the dictionary
# >>> tea_shop["Lemon"] = "green"
# >>> tea_shop["Ginger"]= "sting"
# >>> tea_shop
# {'Masala': 'value', 'Lemon': 'green', 'Ginger': 'sting'}

# how to access or you can say print the dictionary?
# >>> for index in tea_shop:
# ...     print(index)
# ...     
# Masala               // As we can see that its printing only keys
# Lemon
# Ginger          

# how to print the values then?
# >>> for index in tea_shop:
# ...     print(index,tea_shop[index])
# ...     
# Masala value
# Lemon green        // now i can see that keys along with the values gets printed.
# Ginger sting        
# you can use the space, comma, etc while printing we have seen this earlier in list

# different approach of above example is by using the items command
# >>> for key,value in tea_shop.items():   // togethere key and value are treated as items
# ...     print(key,value)
# ...     
# Masala value
# Lemon green
# Ginger sting

# now we will see the nested dictionary
# start with curly brackets
# >>> chai_shop = {"chai":{"Ginger":"one","Lemon":"two","Mint":"strong"},"chai2":{"ginger":"One","lemon":"Two","mint":"Strong"}}
# >>> chai_shop
# {'chai': {'Ginger': 'one', 'Lemon': 'two', 'Mint': 'strong'}, 'chai2': {'ginger': 'One', 'lemon': 'Two', 'mint': 'Strong'}}
# >>> chai_shop.clear()  // to remove the reference completely from the memory
# >>> chai_shop
# {}

# above syntax can also be written in this format
# >>> chai_shop = {
# ... "chai":{"Ginger":"one","Lemon":"two","Mint":"strong"},
# ... "chai2":{"ginger":"One","lemon":"Two","mint":"Strong"}
# ... }
# >>> chai_shop
# {'chai': {'Ginger': 'one', 'Lemon': 'two', 'Mint': 'strong'}, 'chai2': {'ginger': 'One', 'lemon': 'Two', 'mint': 'Strong'}}

# how to access the nested dictionary?
# no issue, access same like normal dictionary.
# >>> chai_shop
# {'chai': {'Ginger': 'one', 'Lemon': 'two', 'Mint': 'strong'}, 'chai2': {'ginger': 'One', 'lemon': 'Two', 'mint': 'Strong'}}
# >>> chai_shop["chai"]
# {'Ginger': 'one', 'Lemon': 'two', 'Mint': 'strong'}
# >>> chai_shop["chai"]["Ginger"]   // now treat previous value as variable and then again ["key"] to get the value
# 'one'


# here you can also use the list comprehension that we have seen earlier
# keep in mind , dictionary need key and value both hence,
# >>> test_dict = {x:x**2 for x in range(10)}   // in front there is written like key:value
# >>> test_dict
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# how to make dictionary from given keys ?
# >>> matrix_chai = ["Ginger","Lemon","Mint"]    // keys matrix
# >>> value_chai = ["default"]     // value matrix
# >>> new_dict = dict.fromkeys(matrix_chai,value_chai)   // we use dict keyword to make sure it make dictionary and 'fromkeys' is the method which take your key matrix and value matrix 
# >>> new_dict
# {'Ginger': ['default'], 'Lemon': ['default'], 'Mint': ['default']}    // all values are same.

# what will happen if i give keys and keys while making the dictionary ?
# >>> new_dict = dict.fromkeys(matrix_chai,matrix_chai)
# >>> new_dict
# {'Ginger': ['Ginger', 'Lemon', 'Mint'], 'Lemon': ['Ginger', 'Lemon', 'Mint'], 'Mint': ['Ginger', 'Lemon', 'Mint']
# As we can see it makes the keys having its own key matrix 