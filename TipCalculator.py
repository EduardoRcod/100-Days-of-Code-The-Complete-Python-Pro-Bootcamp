print("Welcome to the tip calculator!")
bill =float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you lie to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
result = (bill+(bill*(tip/100)))/people
print(f"Each person should pay: ${result:.2f}")