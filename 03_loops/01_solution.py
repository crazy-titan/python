# we have to find the total number of postive intergers from the given array

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_of_positive = 0 #initialise the count with 0

for i in numbers:
    #print(i)    # this will print all numbers one by one
    if i > 0:
        count_of_positive += 1   # for updating the count when we got any positive number
print(count_of_positive)  # always keep in mind about the indentation


