# everyone is thinking of recursion, hey hold on! question is saying to solve using while loop

number = 6 # hardcode value just for understanding
factorial = 1  # because last value to multiple is always 1 not 0

# now come on while loop, where we have to give a true condition to go inside the loop otherwise false never go inside loop
while number > 0:    # i am thinking about each decrement and the last value that will be possible
    factorial = factorial * number
    number = number - 1     # keep on decreasing the value of number
print(factorial)