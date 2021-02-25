#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcome to the tip calculator")
Bill = float(input("What was the total bill? $"))
Tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Total = 1 + (Tip/100)
Num_persons = int(input("How many people to split the bill? "))

Amount_per_person = (Bill / Num_persons ) * Total
Amount_rounded = round(Amount_per_person, 2)
print(f"Each person should pay: ${Amount_rounded}")