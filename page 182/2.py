#Page 182 Question 2
"""
[The factorial of a positive integer n, fact(n), is defined recursively as follows:
        fact(n) 51, when n51
        fact(n) 5n * fact(n21), otherwise
Define a recursive function fact that returns the factorial of a given positive
integer.]
"""

t = int(input("Enter a number: "))

def fact(n):
    if n > 1:
        return n*fact(n-1)
    else:
        return 1

print(fact(t))    
