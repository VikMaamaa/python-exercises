#Page85 Question 4
"""
    [Assume that the variables x and y refer to strings. Write a code segment that prints
    these strings in alphabetical order. You should assume that they are not equal.]
"""

x = (input("Enter a string: ")).lower()
y = (input("Enter a string: ")).lower()

if x < y:
    print(f"1.{x}")
    print(f"2.{y}") 
elif x > y:
    print(f"1.{y}")
    print(f"2.{x}")  
