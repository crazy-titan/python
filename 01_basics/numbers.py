# we will see indepth of numbers in python shell.


# we know operators '+' '-' '*' '/' '%' and '//' for dividing 2 times.


# in begineer stage we can write x + y * z , but in this case we can't able to find which operator is
# working first and not even know about the precision. We most use the paranthesis '()' to define
# which work is completing first, that will give us more precision while calculation.
# Example: >>> x + y * z (wrong practice), (x+y)*z (correct practice)


# Never do operation on different data-types, python is smart it can make you precision. but not always.
# Example: 
# >>> 4 + 2.23
# 6.23
# but if you do like this, then it may be possible than you can make error something like below;
# Example:
# >>> 'chai' + 4
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     'chai' + 4
#     ~~~~~~~^~~
# TypeError: can only concatenate str (not "int") to str


# python treat True and False as '1' and '0'


# when you want to get the output or reference of multiple variable seperated by comma ','
# the output will come as tuple.
# Example:
# >>> x = 2
# >>> y = 3
# >>> z = 4
# >>> x
# 2
# >>> y
# 3
# >>> z
# 4
# >>> x,y,z
# (2, 3, 4)
# We can now do some operation on top of this also
# >>> z-1,x+1
# (3,3)


# operator overloading
# its nothing just the left and right value for an operator '+' , '-' etc it will automatically understand
# if both are same type.
# Example:
# >>> 'chai' + 'hai'
# 'chaihai'
# >>> 


# comparision 
# nothing special its just compare the values as per operator and then output the values.
# Example:
# >>> x
# 2
# >>> y
# 3
# >>> z
# 4
# >>> x < y < z
# True
# How this is happening? (python treat above expression as...)
# >>> x < y and y < z
# True


# python has mystic power to handle the numbers.
# Example: let calculate the power(represented by '**') of a number.
# >>> 100 ** 2
# 10000
# See this now.
# >>> 2 ** 1000
# 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
# it can easliy show value with precison, this is possible in python3 , in python2 little bit 'L' value
# at last to represent that the value is large digit or interger.


# 3 things to search (Learn about this.)
# >>> str('chai')
# 'chai'
# >>> print('chai')
# chai
# >>> repr('chai')
# "'chai'"


# we can also use some type-casting 
# Example:
# >>> int (2.23)
# 2
# >>> float(4)
# 4.0


# result = 1/3.0   not a good practise
# 0.33333333333 this will be the output. We can't store this normally, we will see how to store it later.


# >>> import math
# >>> math.floor(3.5)
# 3
# >>> math.floor(-2.3)
# -3
# floor function make lower value from given value as desire value.
# >>> math.trunc(2.3)
# 2
# >>> math.trunc(-2.3)
# -1 
# trunc is basically help you to go closer to the origin or you can say '0'


# complex numbers
# >>>2 + 3j
# >>> (2 + 3j)*3
# 6 + 9j


# python also handle different base number system ie. binary, hexa and octal
# >>> 0o45
# 37
# >>> 0xAF
# 175
# >>> 0b1000
# 8
# >>> oct(64) ; function to find the octal value of 64
# '0o67'
# >>> hex(65)
# '0x41'
# >>> bin(20)
# '0b10100'


# more good technique is...
# >>> int (64)
# 64
# >>> int(64,8)
# Traceback (most recent call last):
#   File "<python-input-15>", line 1, in <module>
#     int(64,8)
#     ~~~^^^^^^
# TypeError: int() can't convert non-string with explicit base
# >>> int('64',8)
# 52
# >>> int('10000',2)
# 16


# import random
# random.random()         // will give you random values between 0 to 1

# random.randint(a,b)    // it will give you an interger between a and b.
# Example:
# >>> int (64)
# 64
# >>> int(64,8)
# Traceback (most recent call last):
#   File "<python-input-15>", line 1, in <module>
#     int(64,8)
#     ~~~^^^^^^
# TypeError: int() can't convert non-string with explicit base
# >>> int('64',8)
# 52
# >>> int('10000',2)
# 16

# we also have choice option in any array
# >>> l1 =['lemon','masala','ginger','mint']
# >>> random.choice(l1)
# 'ginger'
# >>> random.choice(l1)
# 'lemon'
# >>> random.choice(l1)
# 'masala'

# we can also use for shuffle the cards:
# >>> import random
# >>> l1 = ['lemon','masala','ginger','mint']
# >>> random.shuffle(l1)
# >>> l1
# ['masala', 'ginger', 'lemon', 'mint']
# >>> random.shuffle(l1)
# >>> l1
# ['lemon', 'ginger', 'masala', 'mint']


# for handling the decimal we have decimal library
# Example: you can't add two decimal easily you will get precision error
# 0.1 + 0.1 + 0.1 will give you something weird results. to overcome this , we import Decimal

# >>> from decimal import Decimal
# >>> Decimal('0.1') + Decimal('0.1')
# Decimal('0.2')
# You can search decimal context manager to learn more about this.


# we can also handle fraction similar way
# >>> from fractions import Fraction
# >>> myFrac = Fraction(2,7)             // will give you 2/7
# >>> myFrac
# Fraction(2, 7)


# now come on sets , represented using curly brackets {}.
# here we can do union , intersection , add , subtraction etc.

# >>> setone = {1,2,3,5,7}
# >>> setone & {4,5,9}          // intersection
# {5}
# >>> setone | {4,5,9}
# {1, 2, 3, 4, 5, 7, 9}        // union
# >>> setone - {1,2,3,5,7}
# set()                        // empty set represented like this, also if you want to define empty set, write same 'set()'
# >>> type({})              // empty set is dictionary.
# <class 'dict'>

# more info about python numbers
# >>> True == 1
# True
# >>> True is 1
# <python-input-28>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
#   True is 1
# False
# >>> True + 4
# 5
