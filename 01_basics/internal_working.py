# we will learn the internal working of python.

# a = 5
# b = 3
# a = a + 2
# a will give 7
# b will give 3

# python handle 'numbers' and 'strings' as vip so these can't be collected quickly as garbage.
# Compiler is smart so it wait for some time to collect after de-reference.

# in above syntax first a = 5 will assign than it will go for addition with 2 and then again
# new reference of 7 is alloted to 'a'

# Note:
# python don't have datatypes , but have datatype in memory as reference. 
# for example: score = 10 , it is saying that, in memory there is a reference whose datatype is int
# and it is storing the value 10. where as score is nothing.

# Note:
# List is mutable so, if you write same value , n times than it will act like n different reference.
# where as if you do this same in 'String' and 'number' it will give you same refernce.
# Example:
# >>> usernamee = "chai"
# >>> username  = usernamee
# >>> username
# 'chai'
# >>> usernamee
# 'chai'
# >>> username = "chai"
# >>> username
# 'chai'
# >>> usernamee
# 'chai'
# >>> username is usernamee  // 'is' is a key to check the reference 
# True

# Example:
# >>> one = [1,2,3]
# >>> two = one
# >>> one
# [1, 2, 3]
# >>> two
# [1, 2, 3]
# >>> two = [1,2,3]
# >>> one
# [1, 2, 3]
# >>> two
# [1, 2, 3]
# >>> two is one  // here you can see the reference is different becz list is mutable.
# False
# >>> two == one  // this is just to check the value in both List.
# True
# >>> one[0] = 55
# >>> one
# [55, 2, 3]
# >>> two
# [1, 2, 3]
# >>>                 // this happen because we have given the other reference to 'two'

# Example:
# >>> three = [4,5,6]
# >>> four = three
# >>> three
# [4, 5, 6]
# >>> four
# [4, 5, 6]
# >>> three[0] = 33
# >>> three
# [33, 5, 6]
# >>> four
# [33, 5, 6]
# >>>         // Here you can see that i didn't change the first reference, Hence if i change one
#             // list it will automatically change for 2nd list too. Because they have same ref.



# while assigning the reference inside the memory , Pythone also have a ref count which count the 
# total number of ref and how many are free.

# import sys
# sys.getrefcount() // this will give some big const value always.


# Slicing on List will make a copy and it will be treated as different reference.
# >>> l1 = [1,2,3]
# >>> l2 = l1
# >>> l1
# [1, 2, 3]
# >>> l2
# [1, 2, 3]
# >>> l2 = l1[:]      // slicing will make a copy hence different ref.
# >>> l1
# [1, 2, 3]
# >>> l2
# [1, 2, 3]
# >>> l2 is l1
# False             // because of diff ref.
# >>> l2 == l1
# True            // beause of same values.
# >>> 


# copy is also done using import copy

# import copy
# l2 = copy.copy(l1)     // for copying the value from l1 into l2
# l2 = deepcopy.copy(l1)  // this will be used in case if there is nested list, list inside list.

