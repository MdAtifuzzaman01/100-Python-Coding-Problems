"""
The Problem:
Take two inputs from the user. One will be an integer.
The other will be a float number.
Then multiply them to display the output.
"""
int_text = input("Give an integer number : ")
int_numb = int(int_text)
float_text = input("Give an float number : ")
float_numb = float(float_text)
result = int_numb * float_numb

print("Your result is : ", result)

# Shortcut / Alternative Solution:
"""
You wrote input in one line and then in the next line you used int or float to convert the number.
 You can write the two lines in one line.
"""
int_num = int(input('Give me an integer number: '))
float_num = float(input('Give me a float  number: '))
result = int_num * float_num
print('Your result is: ', result)