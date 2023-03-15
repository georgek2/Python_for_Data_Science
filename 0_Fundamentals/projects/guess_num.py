

number = 8


guess = int(input('Enter your guess: '))


while True:

    if guess == number:
        print('You Win!!')
        break
    elif guess > number:
        print('Guess lower..')

    elif guess < number:
        print('Guess higher..')
        
    else:
        print('Incorrect..')
        break










