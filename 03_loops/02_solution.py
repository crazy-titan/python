user_num = 10   # hardcoded value, assuming 10
sum_even = 0     # sum is zero initially

for i in range(1,user_num + 1):   # because range don't include last value
    if i % 2 == 0:   # checking the number is even or not
        sum_even += i   # update the sum everytime you get an even number.
print("Total sum of even numbers is:",sum_even)