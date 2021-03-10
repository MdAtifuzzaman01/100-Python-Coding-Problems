"""

The problem
Calculate how many days are remaining for the next birthday.
"""


from datetime import  datetime
import time
def get_user_birthday():
    date_str = input('Enter your birth date in DD/MM/YY : ')
    try:
        birthday = datetime.strptime(date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime.datetime(*(time.strptime(date_str, "%d/%m/%Y")[0:6]))

    return birthday


def days_remaining(birth_date):
    now = datetime.now()
    current_year = datetime(now.year, birth_date.month, birth_date.day)
    days = (current_year - now).days
    if days < 0:
        next_year = datetime(now.year + 1, birth_date.month, birth_date.day)
        days = (next_year - now).days
    return days


birthday = get_user_birthday()
next_birthday = days_remaining(birthday)
print("Your birthday is coming in: ", next_birthday, " days")
