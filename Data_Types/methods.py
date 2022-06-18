
'''
    Strings - Working with strings using different methods
    > lower & upper - isupper & islower
    > strip - lstrip & rstrip
    > Capitalize - First letter uppercase
'''

name = 'Lukas Davis'
print(name)
print('Islowercase? : ', name.islower())
print('Isuppercase? : ', name.isupper())

# lower and upper - islower & isupper
name_lower = name.lower()
print('Name in lowercase: ', name_lower)
print('Islowercase? : ', name_lower.islower())

name_upper = name.upper()
print('Name in uppercase: ', name_upper)
print('Isuppercase? : ', name_lower.islower())

# strip - lstrip & rstrip
location = '  New York'
print(location)
print(len(location)) # String length (Location)

loc_stp = location.lstrip()
print(loc_stp)
print(len(loc_stp))

location_2 = 'Washington    '
# location_3 = 'Washington'
print(location_2, '*')
print(location_2.rstrip(), '*')

# Capitalize - First letter uppercase
name_2 = 'john'
print(name_2.capitalize())