input_string = "teeterabab"   # we can see the first char that is non-repeating is 'r'

# to go on 'r' we have to use the loops
for char in input_string:
    # we have seen a count() method in strings to count the value, how many time it is coming
    # we will use that thing here and pass the index in it to find its individual count.
    print(char)
    if input_string.count(char) == 1: # if count will become 1 
        
        print("Char is:",char)     # print that first char

        # but there is slight caches in it, its not optimise , because loops is iterating continuously
        # after getting the first value, but i need only first value, that's why i will use 'break' key
        # word to exit the loop when i got my first char
        break 
        # now break will print only upto 'r', if we don't use the break it will print whole string upto
        # last b char.