
# try to make logics on paper and then code it, it will make you better coder
# we will use the range here same as previous to print the table

# 3 x 1 = 3
# 3 x 2 = 6 

# representation of table as we can see

number = 5   # assuming hard code value 

for i in range(1,11):
    if i == 5:    # condition for checking
        continue     # this will skip the 5th iteration
    print("3","x",i,"=",number*i)   # will output as above prediction format