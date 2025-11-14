"""
Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).
"""
print(int(3.14159)) # Becomes 3

"""
Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.
"""
print(round(3.738492)) # Becomes 4
print(round(3.14159)) # Becomes 3
print(round(3.14159, 2)) # Becomes 3.14

"""
Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
"""
# Addition assignment
score = 5
score += 3  # score is now 8

# Subtraction assignment
score = 5
score -= 2  # score is now 3

# Multiplication assignment
score = 5
score *= 2  # score is now 10

# Division assignment
score = 10
score /= 2  # score is now 5.0

"""
f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.
"""
age = 12

print(f"I am {age} years old")
