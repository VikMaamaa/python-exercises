#Page 85 Question 8
"""[The variables x and y refer to numbers. Write a code segment that prompts the user for
    an arithmetic operator and prints the value obtained by applying that operator to x and y.]
"""

x = (input("Enter 1st number "))
y = (input("Enter 2nd number "))
op = input("Enter Operator ")

ex = x + op + y
result = eval(ex)

print("The result is ",result)
