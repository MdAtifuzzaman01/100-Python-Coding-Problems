"""
 
The problem
For a given string, remove all duplicate characters from that string.
 """

def remove_duplicate(your_str):
    result = ""
    for char in your_str:
        if char not in result:
            result += char
    return result

user_input = input("Enter your string :  ")

no_duplicate = remove_duplicate(user_input)
print('Without Duplicate : ' , no_duplicate)
