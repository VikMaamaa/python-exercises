#Page85 Question 6b
"""[Construct truth tables for the following Boolean expressions:
    b. (not A AND not B)]
"""
#Truth table for (not A AND not B)
#Not gate equivalent, the function acts as a Not gate
def nat(a):
    if a == 0:
        a = 1
        return a
    elif a == 1:
        a = 0
        return a
    
print("A","\tB","\t(NOT A AND NOT B)")
i = 0
x = 0
#i and k are taken as inputs and x as output
for i in range(2):
    j = 0
    while j < 2:
        k = j
        i = nat(i)
        k = nat(k)
        x = (i & k)
        #reverse the values
        i = nat(i)
        k = nat(k)

        #display output    
        print(f"{i} \t{k} \t{x}")
        j +=1
