def cube_sum(num):
    sum = 0
    for n in range( num + 1):
        sum = sum + n**3
    return  sum


user_num = int(input('Enter a number: '))
result = cube_sum(user_num)
print('Your sum of cubes are: ', result)