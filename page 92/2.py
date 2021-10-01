#Page92 Question 2
"""[The factorial of an integer N is the product of the integers between 1 and N, inclusive.
    Write a while loop that computes the factorial of a given integer N.]
 """
 
n = int(input("Enter the number "))

i = 1
f = 1

while i < n + 1:
    f = f * i
    i += 1
    
print(f"The factorial of {n} is {f}")    
