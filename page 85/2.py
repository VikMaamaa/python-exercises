#Page85 Question 2
"""
    [Assume that x refers to a number. Write a code segment that prints the number’s
    absolute value without using Python’s abs function.]
"""

import math
x = float(input("Enter the number: "))
if x < 0:
    x = math.sqrt(x**2)
elif x >= 0:
    x = x
print(f"the absolute value is {x}")    

