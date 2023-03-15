

my_file = open('file.txt', 'w')

my_file.write('This is the first line...')

my_file.close()

# Your name
name = input('Please enter your name: ')

# age
age = input('Your age: ')

# location
location = input('Your location: ')

# likes
profession = input('Your profession: ')


# with open('details.txt', 'a') as file:

#     file.write(f'{name} \n')
#     file.write(f'{age}, \n')
#     file.write(f'{location}, \n')
#     file.write(f'{profession}\n')

print('*'*40)

def details():

    print(f'Name        : {name}')
    print(f'Age         : {age}')
    print(f'Location    : {location}')
    print(f'Profession  : {profession}')


# details()



# Moduler def: 
def create_user(*args):
# def create_user(name, age, location, profession):

    # Create user every time it's called    
    with open('details.txt', 'a') as file:

        file.write(f'{name} \n')
        file.write(f'{age}, \n')
        file.write(f'{location}, \n')
        file.write(f'{profession}\n')


create_user(name, age, location, profession)

