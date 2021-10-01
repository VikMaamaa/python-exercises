#Page 99 Question 2
"""
[Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle.
Recall from the Pythagorean theorem that in a right triangle, the square of
one side equals the sum of the squares of the other two sides.]
"""

a = float(input("Enter the length of side A "))
b = float(input("Enter the length of side B "))
c = float(input("Enter the length of hypothenus, C "))

if (c**2 == a**2 + b**2):
    print("The triangle is a right angle triangle ")
else:
    print("The triangle is not right angle triangle") 
