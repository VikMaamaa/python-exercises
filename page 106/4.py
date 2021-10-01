#Page 106 Question 4
"""[Assume that the variable myString refers to a string, and the variable
reversedString
refers to an empty string. Write a loop that adds the characters
from myString to reversedString in reverse order.]
"""
myString = input("Enter the string ")

reversedString = ""
i = -1
n = len(myString)

while abs(i) <= n:
    reversedString = reversedString + myString[i]
    i -= 1
print(reversedString)
