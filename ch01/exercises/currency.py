rate = input("Please enter current exchange rate for the Euro to Dollar : \n")
amount = input("Please enter an amount you want exchange : \n")
rate = float(rate)
amount = float(amount)
total = (amount * rate)
print(total , "!!BEFORE CHARGE!!")
result = (total - 3)
confirm = input("type yes to continue: \n") 

print(result ,"There is your total")

