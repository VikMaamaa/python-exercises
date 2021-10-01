#Page 118 Question 1
"""
[Assume that the variable data refers to the string "Python rules!". Use a string
method from Table 4-2 to perform the following tasks:
a. Obtain a list of the words in the string.
b. Convert the string to uppercase.
c. Locate the position of the string "rules".
d. Replace the exclamation point with a question mark.]
"""

data = "Python rules!"

#a
ans1 = data.split()
#b
ans2 = data.upper()
#c
ans3 = data.find("rules")
#d
ans4 = data.replace("!", "?")

#Note
"""You can print each variable to see an output if you are test running the program"""
"""e.g print(ans1) """
