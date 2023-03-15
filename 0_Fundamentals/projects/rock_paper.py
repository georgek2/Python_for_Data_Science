
import random 

print('ROCK PAPER SCISSORS GAME')
print('Player Vs Computer')

choices = ['rock', 'paper', 'scissors']

computer = random.choice(choices)

player = input('Enter option: ')

if computer == player:
    print('A Tie')

else:
    print('Someone Wins')


