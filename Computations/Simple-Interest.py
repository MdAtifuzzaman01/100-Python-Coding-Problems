principle = int(input("Money you borrowed: "))
interest_rate = float(input("Interest Rate: "))
time = float(input("Overall Duration: "))

# Calculates simple interest
simple_interest = principle * (interest_rate/100) * time

print("Simple interest is:", simple_interest)