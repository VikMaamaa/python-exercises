#Page 92 Question 3
""" 
    [The log2 of a given number N is given by M in the equation N 5 2M. Using integer
    arithmetic, the value of M is approximately equal to the number of times N can be
    evenly divided by 2 until it becomes 0. Write a loop that computes this approximation
    of the log2 of a given number N. You can check your code by importing the
    math.log function and evaluating the expression round(math.log(N, 2)) (note
    that the math.log function returns a floating-point value).]
"""

N = int(input("Enter the number to find it's log "))

M = 0
L = N 

while N != 1 :
    N = N // 2
    print(N)
    M += 1
print("The log is ",M)     

#This part is use to check the above written code
import math
a = math.log2(L)
a = math.floor(a)
"""math.floor() method was used to test since round() function 
was returning answers that were slightly different by 1"""
print(a)
