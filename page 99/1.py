#Page 99 Question 1
"""
[Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.]
"""

a = float(input("Enter the length of side A "))
b = float(input("Enter the length of side B "))
c = float(input("Enter the length of side C "))

if (c == b == a):
    print("The triangle is an equilateral triangle ")
else:
    print("The triangle is not equilateral") 
