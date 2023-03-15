# Variables = containers to store other datatypes

# String
name = 'Simon'
location ='Globally recognized practitioner'

# Integer
age = 24
worth = 245000000
comp_num = 12j + 2

# Float 
weight = 63.5
results = 0.045

# Booleans
married = False
kind = True

# Print any variable 
# print(name + ' ' + str(results))

#Lists
names = ['lu', 'ja','derick', 'emma', 'john']  
# print(names)

# names[3] = 'jeniffer' 
# print(names[3])

# List out of a dict
d_data = {'name': 'Luke', 'age': 45, 'height': 165.3}

print(d_data)

# print(list(d_data))
# print(list(d_data.values()))

'''
    Tuples
'''
likes = ('hockey', 'restling', [1, 2, 3], 'swimming', 'networking', 'singing')
# print(likes[2])
likes[2][1] = 'jogging'

# print(likes[2])

d_data = {'name': 'Luke', 'age': 45, 'height': 165.3}

# print(d_data)

print(tuple(d_data))
print(tuple(d_data.values()))


# Looping through
# for name in names:
#     print(name)

# for like in likes:
#     print(like)




'''
    Sets
'''
items_list = ['A', 'B', 'B', 'C', 'D', 'D']

print(items_list)
print(set(items_list))

# items = {'username', 34, 23.32, {1, 3, 4}}
# items
# print(items)



'''
    Dictionaries
'''
details = [['name', 'Elvis'], ['age', 78]]

a_dict = dict(details)

print(a_dict)


