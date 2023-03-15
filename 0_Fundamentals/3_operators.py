'''
    Operators

    > Addition + 
    > Subtraction -
    > Multiplication *
    > Division / & //
'''

'''
    Addition
'''
# Strings

first_name = 'Amazon ' #Notice the trailing space here
last_name = 'Forest'
full_name = first_name + last_name
print(full_name)

first = 'Farhan is ' #Notice trailing space
age = 34
last = ' years old' #Notice the space at the beginning
full_sttm = first + str(age) + last
print(full_sttm)

name = 'Anna '
likes = {'travelling', 'reading', 'hiking'}
full = name + str(likes)
print(full)


# Lists

names = ['first', 'second']
nums = [23, 54, 34]

conc_list = names + nums

print(conc_list)

print('*'*40)

# Tuples

items_1 = ('first', 'second')
items_2 = ('third', 'fourth', 45.98)

full_tuple = items_1 + items_2
print(full_tuple)


# Sets

set_1 = {22, 34, 56}
set_2 = {78, 33}

# full_set = set_1 + set_2
# print(full_set)


# Objects
object_1 = {1: 'one', 2: 'two'}
object_2 = {3: 'three', 4: 'four'}


# full_obj = object_1 + object_2

# print(full_obj)

# Trying to add tuple + list

# combo = names + items_1

# print(combo)


'''
    Subtraction
'''

# Strings

str_1 = 'first_name'
str_2 = 'last_name'

# print(str_1 - str_2)

# Lists
nums_1 = [23, 54, 34]
nums_2 = [73, 24, 30]


# print(nums_1 - nums_2)


# Tuples
# nums_1 = (23, 54, 34)
# nums_2 = (25, 24, 34)

# print(nums_1 - nums_2)

# Sets
set_a = {'A', 'B', 'D'}
set_b = {'B', 'C', 'A'}

print(set_a - set_b) # Outputs items in nums_1 that are not in nums_2


'''
    Multiplication *
'''
# Can only multiply sequence or collection with an integer
# Strings 
# print(str_1 * str_2)


# Strings & Integers

statement = 'I like apples '
nums = 2
print(statement * nums) 


# Tuples & Tuples
# print(nums_1 * nums_2)

# Tuples & Integers
numbers = (23, 54, 34)
print(numbers * 3)


# Lists & Ints
likes = ['reading', 'football', 'driving']

print(likes * 3)
# print(likes * likes) # Can't * list & a list

# Sets & Ints
set_likes = {'reading', 'football', 'driving'}

# print(set_likes * 2)
# print(set_likes * set_likes)


# Objects
object_1 = {1: 'one', 2: 'two'}
object_2 = {3: 'three', 4: 'four'}

# print(object_1 * 2) # Unsupported..!!

# print(nums_1 / 2)
0703417646

'''
    Division
'''
int_1 = 4
int_2 = 2

print(int_1 / int_2)


print(int_1 // int_2)


print('*'*40)
'''
    Comparison
    > Equals ==
'''

# Equals
# String
statement = 'I like apples '
sttm_2 = 'I like apples '
sttm_3 = 'I like apples'
sttm_4 = 'i like apples'

# print(statement == sttm_2)
# print(statement == sttm_3) # Spaces in strings matter
# print(statement == sttm_4) # Lowercase & Uppercase

# Numbers
num_1 = 20
num_2 = 20.0 # Zero as the only decimal has no effect
num_2 = 20.1

# print(num_1 == num_2)
# print(num_1 == num_2)


# Collections
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3]
list_3 = [1, 2, 4]
list_4 = [1, 2, 'three']

# print(list_1 == list_2)
# print(list_1 == list_3)
# print(list_1 == list_4)

names_1 = ['one', 'two', 'three']
names_2 = ['one', 'two', 'three']
names_3 = ['one', 'two', 'four', 'five']

# print(names_1 == names_2)
# print(names_1 == names_3)
1
# Sets
set_1 = {'first', 'second'}
set_2 = {'first', 'second'}
set_3 = {'first', 'second', 'second'}
set_4 = {'first', 'second', 'third'}

# print(set_1 == set_2)
# print(set_1 == set_3) # True since it ignores the duplicate
# print(set_1 == set_4)

# Object
obj_1 = {1: 'first', 2: 'second'}
obj_2 = {1: 'first', 2: 'second'}
obj_3 = {1: 'first_', 2: 'second'}
obj_4 = {3: 'three', 4: 'four'}

# print(obj_1 == obj_2)
# print(obj_1 == obj_3)
# print(obj_1 == obj_4)



'''
    Greater than or Equal to ( >= )
'''

# print(names_1 > names_3)

num_1 = 499
num_2 = 49.9

print(num_1 >= num_2)









