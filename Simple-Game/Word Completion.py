"""
The Problem
Build a simple word completion game.

You will be given a partial word with hyphens. It’s a clue to an actual word. For example,

-a-e

Now you have to provide a word that matches with the exposed letters. If you provide any of these words- “game” or “fame” or “lame”, your answer will be correct.

Because all these words have the letter “a” in the second position and the letter “e” in the fourth position.

So, the idea is, your provided word has to have the same letter as the clue.
"""



import random


def get_a_clue():
    clues = ['-a-e', 'y-ll-w', 's-mm-r', 'wi-t-r', 's-n-y', 'l-v-', '-i-e']
    position = random.randint(0, len(clues) - 1)
    clue = clues[position]
    return clue


def check_word_match(clue, guess):
    if len(clue) != len(guess):
        return False
    for i in range(len(clue)):
        if clue[i] != '-' and clue[i] != guess[i]:
            return False
    return True


# start the game
word_clue = get_a_clue()
print('Your word clue:', word_clue)
answer = input('What would be the word: ')

is_matched = check_word_match(word_clue, answer)

if is_matched is True:
    print('WOW!!! You win')
else:
    print('Opps! you missed it.')