distance = 5 # you can take it from user also i am just taking hardcode value for now.

if distance < 3:
    transport = "Walk"
elif distance < 15:
    transport = "Bike"
else:
    transport = "Car"

print("Hello,use",transport,"as you transport.")