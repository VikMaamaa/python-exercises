#Page 106 Question 3
"""[Assume that the variable myString refers to a string. Write a code segment that
uses a loop to print the characters of the string in reverse order.]
"""

myString = str(input("Enter the string: "))

for i in range(len(myString)):
    j = i
    j += 1
    j *= -1
    print(myString[j])

#Note you can also use the pattern used in question 4 to bypass the problem of 
# Negative Sign i.e 'abs(counter)'