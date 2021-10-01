#Page 145 Question 2
"""[Assume that the variable data refers to the list [5, 3, 7]. Write the expressions
that perform the following tasks:
a. Replace the value at position 0 in data with that value’s negation.
b. Add the value 10 to the end of data.
c. Insert the value 22 at position 2 in data.
d. Remove the value at position 1 in data.
e. Add the values in the list newData to the end of data.
f. Locate the index of the value 7 in data, safely.
g. Sort the values in data.]
"""
data = [5, 3, 7]

#a
data[0] = -1 * data[0]
#b
data.append(10)
#c
data.insert(2, 22)
#d
data.remove(data[1])
#e
data.append(newData)
"""
[If you want to test run the code you have to create a list named 'newData']
"""
#f
data.index(7)
#g
data.sort()
print(data)
