import random

value = random.randint(1,3)
bot = ''

if value == 1:
    bot = 'scissors'
elif value == 2:
    bot = 'paper'
elif value == 3:
    bot = 'rock'

player_input = input('Enter player input ROCK PAPER OR SCISSORS')
while player_input != 'paper' and player_input != 'rock' and player_input != 'scissors':
    player_input = input('Enter player input ROCK PAPER OR SCISSORS, again')


print(bot)
if player_input == 'rock':
    if bot == 'paper':
        print('bot won')
    elif bot == 'rock':
        print('tie')
    elif bot == 'scissors':
        print('YOU WON')
elif player_input == 'paper':
    if bot == 'paper':
        print('tie')
    elif bot == 'rock':
        print('YOU WON')
    elif bot == 'scissors':
        print('you lost')
elif player_input == 'scissors':
    if bot == 'paper':
        print('YOU WON')
    elif bot == 'rock':
        print('you lost')
    elif bot == 'scissors':
        print('tie')
