#Here we are gonna calculate the average number of the grades of 5 subjects and then calculate the grade.
print("Enter your marks")
sub1= int(input("First Subject : "))
sub2= int(input("Second Subject : "))
sub3= int(input("Third Subject : "))
sub4= int(input("Fourth Subject : "))
sub5= int(input("Fifth  Subject : "))
avg = (sub1 + sub2 + sub3 + sub4 + sub5 )/5

if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
else:
    print("Grade: F")

