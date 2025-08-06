# Question is saying to keep asking the same question again n again if user don't input the value
# between 1 and 10 , so to make this we will use the while loop

while True:  # for keep on iteration inside loop no limit, as mentioned in question to ask again n again
    # taking input here
    number = int(input("Enter your number: "))
    if 1 <= number <= 10:   # in single line you can check both conditions
        print("Thanks")
        break # because we have to exit the loop once input is between 1 and 10
    else:
        print("Enter a Valid Number,Try Again...")