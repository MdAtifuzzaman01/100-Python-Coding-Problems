"""

The problem
Reverse the word in a sentence.
"""

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return  " " .join(words)


user_input = input('Enter a sentence :')
reverse = reverse_words(user_input)
print('Reversed words : ', reverse)