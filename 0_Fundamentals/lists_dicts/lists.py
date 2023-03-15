
'''
    Comprehensive guide to python lists
    > Methods
    > Data Access and Manipulation

'''

# A collection of ordered items
numbers = [11, 22, 22, 55]

'''
    Methods
    > Append    : Add item at the end of the list
    > Insert    : Add item at a specific index
    > Extend    : Add all elements in a given iterable to the list

    > Pop       : Remove last item in the last
    > Remove    : Delete a specific item from the list

    > Count     : Count the number of times an item appears in the list
    > Index     : Find the position of the first occurence of a given item


'''
print(numbers)

# Append 77
numbers.append(77)
# print(numbers)

# Insert 99
numbers.insert(0, 99) # Start with the index, then item to be added
# print(numbers)

# Extends
nums = [88, 88, 33, 66]
numbers.extend(nums) 

print(numbers)


# Pop - 66
numbers.pop()

print(numbers)


# Remove - 22
numbers.remove(22) # REmoves the first occurence of 22

print(numbers)


# Count
print(f'Number of 88s: {numbers.count(8)}')


# Index - 55, 88
print(f'Index of 55: {numbers.index(55)}')
print(f'Index of 88: {numbers.index(88)}')

likes = ['hiking', 'reading', 'watching']

# Access item at index 1
likes[1]

# likes.e








