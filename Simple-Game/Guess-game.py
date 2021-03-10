"""

The Problem
Build a simple guessing game where it will continuously ask the user to enter a number between 1 and 10.

If the user's guesses matched, the user will score 10 points, and display the score. If the users' guess doesn’t match display the generated number.

Also, if the user enters “q” then stop the game.
"""

import random
print('To stop the game enter q')
score = 0
while True:
    num = random.randint(0,10)
    guess = input("Guess a number between 1 and 10 : ")
    if guess == "q":
        print('Game over!')
        break

    guess_num = int(guess)
    if guess_num is num:
        print('Congrats ! You guessed it correctly')
        score += 10
        print("Your new score: " , score)
    else:
        print('Incorrect guess')
        print('The number was : ' , num)



