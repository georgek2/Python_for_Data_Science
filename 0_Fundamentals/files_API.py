'''
    Call an API that provides dummy customer data to work with
    > Store data into a text file

''' 

# api_content = request_data.

# API data
data = {
    'name': 0,
    'age': 0,
    'location': 0,
    'profession': 0
}


# Your name
name = input('Please enter your name: ')
name = data['name'] # API data

# age
age = input('Your age: ')
age = data['age']

# location
location = input('Your location: ')
location = data['location']

# likes
profession = input('Your profession: ')
profession = data['profession']





# Moduler def: 
def create_user(*args):
# def create_user(name, age, location, profession):

    # Create a new user every time it's called    
    with open('details.txt', 'a') as file:

        file.write(f'{name} \n')
        file.write(f'{age}, \n')
        file.write(f'{location}, \n')
        file.write(f'{profession}\n')


create_user(name, age, location, profession)

