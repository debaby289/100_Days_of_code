"""
We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:
(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60

Demo
https://appbrewery.github.io/python-day2-demo/

Very Optional Reading: Floating Point Arithmetic
https://docs.python.org/3/tutorial/floatingpoint.html
"""
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculate the tip as a percentage
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill *  tip_as_percent

# Calculate the total bill including the tip
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay
bill_per_person = total_bill / people

# Round the amount to 2 decimal places
final_amount = round(bill_per_person, 2)

# Format the final amount to 2 decimal places as a string
print(f"Each person should pay: ${final_amount}")


