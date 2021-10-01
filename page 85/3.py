#Page85 Question 3
"""
    [Write a loop that counts the number of space characters in a string. Recall that the
    space character is represented as ' '.]
"""


x = input("Enter the String: ")
n = 0
for i in range(len(x)):
    if x[i] == ' ':
        n += 1
print(f"The number of space in the string is {n}")        
