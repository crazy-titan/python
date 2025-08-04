no_of_char = 6

if no_of_char < 6:
    password = "Weak"
elif no_of_char <= 10:
    password = "Medium"
else:
    password = "Strong"

print("Your password is:",password)