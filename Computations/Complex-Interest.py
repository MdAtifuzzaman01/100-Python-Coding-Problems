"""

The Problem:-
Take money borrowed, interest and duration as input. Then, compute the compound interest rate.
"""


def compound_interest(principle, rate, time):
    interest = principle * ((1 + rate / 100) ** time)
    return interest


principle = int(input("Money you borrowed : "))
interest_rate = int(input("Interest rate : "))
time = float(input("Total Duration : "))


total_due = compound_interest(principle , interest_rate , time)

print("Interest amount is : ", total_due)