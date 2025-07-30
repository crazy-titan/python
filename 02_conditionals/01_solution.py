# first of all we learn the input command
# which will get the user input from the command line
# use python shell to know about the 'input' command

# >>> user_points = input("Give me any number: ")
# Give me any number: 10
# >>> user_points
# '10'
# >>> user_points / 2
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     user_points / 2
#     ~~~~~~~~~~~~^~~
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# >>> user_points_in_int = int(user_points)
# >>> type(user_points_in_int)
# <class 'int'>
# >>> type(user_points)
# <class 'str'>
# >>> user_points_in_int / 2 
# 5.0


# NOW LETS SOLVE THE QUESTIONS

user_age = int(input("Give me you age: "))   # directly convert into integer

if user_age < 13:      # check if its less than 13
    print("Child")
elif user_age < 20:     # you can also use elseif but use short notations 'elif'
    print("Teenager")
elif user_age < 60:
    print("Adult")
else:
    print("Senior")