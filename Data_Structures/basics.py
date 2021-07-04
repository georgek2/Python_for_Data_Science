# Variables = containers to store other datatypes

# String
name = 'George'
location ='Globally recognized practitioner'

# Integer
age = 24
worth = 245000000

# Float 
weight = 63.5
results = 0.045

# Booleans
married = False
kind = True

# Print any variable 
# print(name + ' ' + str(results))

#Lists and tuples
names = ['luke', 'jane', 'derick', 'emma', 'john']
# print(names)

names[3] = 'jeniffer'
# print(names[3])

likes = ('hockey', 'restling', [1, 2, 3], 'swimming', 'networking', 'singing')
# print(likes[2])
# likes[1] = 'jogging'

# print(likes[2])

# Looping through
# for name in names:
#     print(name)

for like in likes:
    print(like[0:1])