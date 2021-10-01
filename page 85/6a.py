#Page85 Question 6a
"""[Construct truth tables for the following Boolean expressions:
    a. not (A or B)
    ]
"""

#Truth table for not(A or B)
print("A","\tB","\tNOT(A OR B)")
i = 0
x = 0

#i and j are taken as inputs and x as output
for i in range(2):
    j = 0
    while j < 2:
        #OR gate operation
        x = (i | j)
        
        #Not gate equivalent
        if x == 0:
            x = 1
        elif x == 1:
            x = 0
            
        #display output    
        print(f"{i} \t{j} \t{x}")
        j +=1
