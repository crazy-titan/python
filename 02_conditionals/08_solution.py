no_of_char = 6

if no_of_char < 6:
    password = "Weak"
elif no_of_char <= 10:
    password = "Medium"
else:
    password = "Strong"

print("Your password is:",password)

# The second method for solving this is by using the 'len' function.

password = "san@Abh4518"  # let's assume something random that you got from the user input.

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Hard"

print("Password that you have set is: ",strength)

# some of you can thing that , why we are calculating len again and again.
# so you can optimise it by initialise a new variable ie. length_pass = len(password) and then use it at the place of len(password) everywhere.