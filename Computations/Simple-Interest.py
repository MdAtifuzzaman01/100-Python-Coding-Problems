"""
The Problem
You borrowed $1000 for 1 year with 2% interest per year.
Calculate the simple interest to know how much you have to pay?
"""

# Solution:
principle = int(input("Money you borrowed : "))
interest_rate = int(input("Interest Rate : "))
time = float(input("Total Duration : "))

# Calculates simple interest

simple_interest = principle * (interest_rate / 100) * time

print("Simple interest is :", simple_interest)