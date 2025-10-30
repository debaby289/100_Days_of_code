"""
Create a greeting for your program.
Ask the user for the city that they grew up in and store it in a variable.
Ask the user for the name of a pet and store it in a variable.
Combine the name of their city and pet and show them their band name.
Make sure the input cursor shows on a new line after the question
Demo: https://appbrewery.github.io/python-day1-demo/
"""
#Greeting message
print("Welcome to the generator!")

#City and Pet variable creation
city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")

#Band name
band_name = city + " " + pet
print(f"Your band name could be: {band_name}")
