user_score = int(input("Mention your score:"))

# if user_score >= 90:
#     grade = 'A'
# elif user_score >= 80:
#     grade = 'B'
# elif user_score >= 70:
#     grade = 'C'
# elif user_score >= 60:
#     grade = 'D'
# elif user_score >= 50:
#     grade = 'E'
# else:
#     grade = 'F'

# print("Your Grade is:",grade)
# IN ABOVE CODE THERE IS AN ISSUE IF SOMEONE INPUT MORE THAN 100, then it can't be possible.
# To overcome this issue we use a conditional after taking the input.

# if user_score >= 101:
#     print("Enter a Valid score")

# but problem still there because it will output as "Enter a Valid score" and also some grade
# because we didn't exit the conditional , to do that we use exit() to break the conditional.

if user_score >= 101:
     print("Enter a Valid score")
     exit()
if user_score >= 90:
    grade = 'A'
elif user_score >= 80:
    grade = 'B'
elif user_score >= 70:
    grade = 'C'
elif user_score >= 60:
    grade = 'D'
elif user_score >= 50:
    grade = 'E'
else:
    grade = 'F'

print("Your Grade is:",grade)