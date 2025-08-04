# just read the problem and try to understand it.

year = int(input("Enter any Year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year," is a LEAP Year.")
else:
    print(year," is NOT a Leap Year.")
