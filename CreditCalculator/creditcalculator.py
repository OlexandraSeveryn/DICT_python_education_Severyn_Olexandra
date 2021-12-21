import math
print("Enter the loan principal:")
principal = int(input(">"))
print("What do you want to calculate?")
print('type "m" – for number of monthly payments,')
print('type "p" – for the monthly payment:')
type = input(">")

if type == "n":
    print("Enter the monthly payment:")
    payment = int(input(">"))
    count_month = math.floor(principal/payment)
    print(f"It will take {count_month} months to repay the loan")
elif type == "p":
    print("Enter the number of months:")
    period = int(input(">"))
    payment = principal/period
    if payment %1 > 0:
        payment = math.ceil(payment)
        lastpayment = principal-(period-1)*payment
        print(f"Your monthly payment = {payment} and the last payment = {lastpayment}.")
    else:
        print(f"Your monthly payment = {payment}")