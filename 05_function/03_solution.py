# Polymorphism is something which handle one or more things in same mannar
# >>> 5 * 5
# 25
# >>> 'a' * 5
# 'aaaaa'

# above explanation of polymorphism

def multipy(num1,num2):
    return num1 * num2

print(multipy(5,5))
print(multipy('a',5))   # same output
print(multipy(5,'a'))   # same output 
