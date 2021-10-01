price = int(input("Enter the Purchase Price: "))
rate = 0.12
balance = 0
total_balance = price - (0.1 * price)
monthlyPayment = (0.05 * price) - (0.1 * price)

i = 1

print("Month","\tCurrent Total Balance","\tInterest","\tPrincipal","\tPayment","\tBalance")
while total_balance > 0:
    if i == 1 :
        monthlyInterest = int(total_balance * (rate / 12))
        monthlyPrincipal = int(monthlyPayment - monthlyInterest)   
    else:    
        monthlyInterest = int(balance * (rate / 12))
        monthlyPrincipal = int(monthlyPayment - monthlyInterest) 
    
    print(f"{i}\t{total_balance}\t{monthlyInterest}\t{monthlyPrincipal}\t{monthlyPayment}\t{balance}")
    
    balance = total_balance - monthlyPayment
    # total_balance = balance
    i = i + 1
