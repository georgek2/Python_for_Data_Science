

'''
    Control Flow
    > IF, ELIF, ELSE
    > FOR & WHILE


    Functions
    > Define a def
    > Calling a function
'''


# IF, ELSE, ELIF

name = 'Anna'
age = 19

if age >= 18:
    print('Allowed to register...')

else:
    print('Restricted access! - Minor')


weather = 'rainy'

if weather == 'rainy':
    print('Carry umbrella and jacket')

elif weather == 'sunny':
    print('No need for a jacket')

elif weather == 'windy':
    print('Wear a heavy jacket')

else:
    print('Wear a light jacket')



print('*'*50)


# FOR

inventory = ('mangoes', 'bananas', 'apples', 'tomatoes')

# Grab each item one at a time
# for item in inventory:

#     print(item)


# nums = [10, 20, 30, 40]
# new_list = list()

# for num in nums:

#     item = num * 2

#     new_list.append(item)

# print(nums)
# print(new_list)



# While

# game_on = True

# while game_on:

#     print('Player continues playing')
#     print('Until they lose or win the game...!!')

#     # Stop the loop
#     game_on = False


# Functions

# result = 'Right foot up, Left foot slide...'

def the_func_name():

    result = 'The expected function ouput'

    return result 


print(the_func_name())



# Welcome message

def welcome():

    print('Welcome! Welcome! To the Feast of Fury..#')


# welcome()

def welcome():

    message = 'Welcome! Welcome! To the Feast of Fury..#'

    return message

# print(welcome())

# Multiply a * b
# Arguments required
def multiply(a, b):

    return a * b


# print(multiply(12, 5))

# print(multiply('12', 5))


# Say Hello to a user

def sayHello():

    name = input('Enter your name: ')

    result = 'Hello ' + name

    return result

# print(sayHello())



# Function to display items

def displayItems(collection):
 
    print('The items needed are: ')

    for item in collection:

        print('> ' + item)

displayItems(inventory)



# Simple guessing game

def guessNum():

    num = 8
    count = 3
    # Wrap the input data above inside the int() to convert it to a number

    game_over = False

    while game_over == False:

        while count > 0:
            count = count - 1
            guess = int(input('Enter your guess (1 - 10): ')) 
            if guess == num:
                print('Correct...!!')
                game_over = True

                break

            else:

                print('Wrong.!! Guess again')

                break


guessNum()












