#Page 99 Question 6
"""[The German mathematician Gottfried Leibniz developed the following method
    to approximate the value of :
            /4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .#'please check the textbook to view the series properly'
    Write a program that allows the user to specify the number of iterations used in
    this approximation and that displays the resulting value.]
"""
n = int(input("Specify the number of iterations: "))

sumL = 0 #sumL is the variable that stores the result of the series

for i in range(n):
    f = ((-1)**i) / ((2*i) + 1) #this is the formula used to generate the series
    sumL += f
    
print(sumL*4)  #from the formula to get the value of PI you need to multiply sumL by 4  
