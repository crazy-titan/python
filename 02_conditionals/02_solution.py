user_age = int(input("Give me your age:"))
day = "Wednesday"  # let's give a hardcoded value

price = 12 if user_age >= 18 else 8   # excellent and new syntax see again
# its like set the price as 12 if user_age is greater than 18 else set as 8

# now check for the day

if day == "Wednesday":
    # price = price - 2
    price -= 2            # another way to represent price = price - 2

print("Ticket price is: $",price)  # more good way of representation

