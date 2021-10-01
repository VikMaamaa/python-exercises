#Page 145 Question 5
"""[Assume that data refers to a list of numbers, and result refers to an empty list.
Write a loop that adds the nonzero values in data to the result list, keeping them
in their relative positions and excluding the zeros.]
"""

data = [3,4,0,5,7,0] #- this list was used for test running
result = []

for i in range(len(data)):
    if data[i] != 0 :
        result.append(data[i])

print(result)        
