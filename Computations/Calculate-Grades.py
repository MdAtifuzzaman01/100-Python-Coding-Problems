"""
The problem:
Calculate grade of five subjects.
"""
# Solution:-

print("Enter your marks : ")
sub_1 = int(input('1st Subject : '))
sub_2 = int(input('2nd Subject : '))
sub_3 = int(input('3rd Subject : '))
sub_4 = int(input('4th Subject : '))
sub_5 = int(input('5th Subject : '))

average = (sub_1 + sub_2 + sub_3 + sub_4 + sub_5)/5

if average >= 90:
    print('Grade A')
elif average >= 80:
    print("Grade B ")
elif average >= 70:
    print('Grade C')
elif average >= 60:
    print('Grade D')
else:
    print('Grade F')



