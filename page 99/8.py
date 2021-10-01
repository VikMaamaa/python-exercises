#Page 99 Question 8
"""[The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. 
Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers. You can use this algorithm in the 
following manner:
a. Compute the remainder of dividing the larger number by the smaller
number.
b. Replace the larger number with the smaller number and the smaller number
with the remainder.
c. Repeat this process until the smaller number is zero.
The larger number at this point is the GCD of A and B. Write a program that lets the user enter two integers and then prints each step 
in the process of using the Euclidean algorithm to find their GCD.]
"""
a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))

smaller = 0 ,larger = 0, remainder = 0
if a > b : #This part determines which number is the largest, s is used to store smallest number, l the larger
    smaller = b
    larger = a
    print("check")
elif a < b :
    smaller = a
    larger = b
    print("check")

while True :
    if smaller == 0: #This part checks wether the smaller number is zero
        break
    else:
        remainder = larger % smaller #This part computes the remainder
        larger = smaller
        smaller = remainder  

print(f"The GCD of {a} and {b} is {larger}")