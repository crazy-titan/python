# python use 'def' keyword to define the function

def square(number):
    print(number ** 2)   # this will print automatically

sq = square(4)   # called the function and it will print automactially
print(sq) # here print is none , because there is print statement in def
                # which is not returning anything just printing

# see other example

def square_of_num(number):
    return number ** 2

print(square_of_num(4))    # now you will get 16 only
sum = square_of_num(4)
print(sum)    # here we can do like this because def is returning the value and i am storing it