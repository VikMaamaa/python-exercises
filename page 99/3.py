#Page 99 Question 3
"""[Modify the guessing-game program of Section 3.5 so that the user thinks of a
number that the computer must guess. The computer must make no more than
the minimum number of guesses, and it must prevent the user from cheating by
entering misleading hints. (Hint: Use the math.log function to compute the minimum
number of guesses needed after the lower and upper bounds are entered.)]
"""
import random
import math

smaller = int(input("Enter the smaller number: "))
larger  = int(input("Enter the larger number: "))
userNumber = int(input("Enter Number to be guessed: "))
#This part generate the minimum number of guesses
mil = (larger - smaller) + 1
minGuess = math.log(mil, 2)
minGuess = math.floor(minGuess)

count = 0
while count <= minGuess:
    count += 1
    myNumber = random.randint(smaller, larger)
    print(myNumber)
    if  myNumber< userNumber:
        print("Too small!!")
        print("The Computer is guessing again!")
    elif myNumber >  userNumber:
        print("Too large!!")
        print("The Computer is guessing again!")
    else:
        print("The Computer have got it in",count,"tries")
        break        
