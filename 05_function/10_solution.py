def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

print(factorial(5))

# in recursive functions , always think about the exit conditions , if you find exit thinking
# you are good at recursion , its a good topic in DSA.  