#Page 145 Question 6
"""[Write a loop that replaces each number in a list named data with its absolute value.]"""

data = [3,4,-10,5,-7,-2] #- this list was used for test running

for i in range(len(data)):
    data[i] = abs(data[i])
    
print(data)    
