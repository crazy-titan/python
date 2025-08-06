# assuming, user is giving input as interger only

number = 28
is_prime = True  # assuming its prime initially

# how to think about logic?
# for a prime number, it should be greater that 1 and should be divisible by itself only.
# also it should not be divisible by any number in the range 2 to 'number'
# why 2?
# because 1 will divide every number 

if number > 1:
    #now we have to check from 2 to 'number', to do that we use loops
    for i in range(2,number): # we are not using number+1 because if it can't find any in range than its 
    # prime automatically, and prime divisible by itself
        if (number % i) == 0:
            is_prime = False    # if divide than its not a prime
print(is_prime)