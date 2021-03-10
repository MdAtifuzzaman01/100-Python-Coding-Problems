"""

The Problem
Create a bulls and cows game for guessing a randomly generated 4 digits number.
"""

import random

secret_number = str(random.randint(1000 , 9999))
print('Guess the number . It contains 4 digits')

remaining_try = 7

def get_bulls_cows(number , user_guess):
    bulls_cows = [0,0] #cows , then bulls
    for i in range(len(number)):
        if user_guess[i]  == number[i]:
            bulls_cows[0] += 1
        elif user_guess[i] in number:
            bulls_cows[1] +=1
    return bulls_cows

while remaining_try > 0:
    player_guess = input('Enter your guess : ')

    if player_guess == secret_number:
        print('Yay ! You guessed it correctly')
        print('You win')
        break
    else:
        bulls_cows = get_bulls_cows(secret_number , player_guess)


        print('Bulls : ' , bulls_cows[0])
        print('Cows : ' , bulls_cows[1])

        remaining_try -=1
        if remaining_try < 1:
            print('You lost the game !')
            break


