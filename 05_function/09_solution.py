#  yeild is used to store the reference and state of the function in memory
# in place of return to stop ending the function

def even_generator(limit):
    return range(2,limit+1,2) # range is exclusive 

print(even_generator(10)) #range(2, 11, 2) will be the output


###


def even_generator(limit):
    for i in range(2,limit+1,2): # range is exclusive
        print(i) 

print(even_generator(10)) # will give 2,4,6,8,10


### we don't want to print


def even_generator(limit):
    for i in range(2,limit+1,2): # range is exclusive
        return i 

print(even_generator(10)) # will give none and 2,4,6,8,10 as we have seen earlier.


### Then how to get the value? list?


def even_generator(limit):
    li = []
    for i in range(2,limit+1,2): # range is exclusive
        li.append(i)
    return li

print(even_generator(10))  # will give the list, which i don't need


### How to do this then ?


def even_generator(limit):
    for i in range(2,limit+1,2): # range is exclusive
        yield i

print(even_generator(10))  # giving us a memory address, <generator object even_generator at 0x100b297e0>


# is this iterable?

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)   # will get my answer perfectly now