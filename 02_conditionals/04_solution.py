fruit = "Banana"
color = "Brown"

# we have taken hardcoded values just similar to what question is saying

if fruit == "Banana":   # checking and single '=' is assignment
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":   # we didn't used the else because we have a particular value 'brown'
        print("Overripe")