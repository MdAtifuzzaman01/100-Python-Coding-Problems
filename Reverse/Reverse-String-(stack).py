"""

The Problem
Reverse a string using a stack.
"""

def reverse_stack(str):
    stack =[]

    for char in str:
        stack.append(char)


    rev = ''
    while len(stack) > 0:
        last = stack.pop()
        rev = rev + last
        # print(last, rev)

    return rev


usr_str = input('What is your string:')
reverse = reverse_stack(usr_str)
print('Reversed is: ', reverse)


