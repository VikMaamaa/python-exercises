#Page 106 Question 2
"""[Assume that the variable data refers to the string "myprogram.exe". Write the
expressions that perform the following tasks:
a. Extract the substring "gram" from data.
b. Truncate the extension ".exe" from data.
c. Extract the character at the middle position from data.]
"""

data = "myprogram.exe"

#a
data[5:9]
#b
data = data[:10]
#c
data[7]
