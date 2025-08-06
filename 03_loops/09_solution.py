items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()  # because set only contains unique value, and don't take any duplicates

# to access each values/index of the list items, we have to iterate one by one on it
# for that we use for loop

# after that i will check if the index value is present in my unique_item set or not
# that will give me true or false value, if true just break and if false add it into the set


for i in items:
    if i in unique_items:
        print("Duplicate")
        break
    else:
        unique_items.add(i)
print(unique_items) # check what is there in set



# the above code can also be written as below
# for i in items:
#     if i in unique_items:
#         print("Duplicate")
#         break
#     unique_items.add(i)
# print(unique_items) # check what is there in set

# both are same