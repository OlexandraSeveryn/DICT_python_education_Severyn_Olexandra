import math
print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')

type = input(">")

if type == "n":
    print("Enter the loan principal:")
    principal = int(input(">"))
    print("Enter the monthly payment:")
    payment = int(input(">"))
    print("Enter the loan interest:")
    percent = int(input(">"))/100.0
    i = percent/(12*1)

    n = math.log(payment/(payment-i * principal), 1+i)
    n = math.ceil(n)
    year = n/12
    if year %1 > 0 :
        month = (year%1)*12

        year = int(year)
        month = int(month)

        if month == 0:
            print(f"It will take {year} years to repay this loan!")
        elif year == 0:
            print(f"It will take {month} months to repay this loan!")
        else:
            print(f"It will take {year} years and {month} months to repay this loan!")
    else:
        print(f"It will take {year} years to repay this loan!")




elif type == "a":
    print("Enter the loan principal:")
    principal = float(input(">"))
    print("Enter the number of periods:")
    period = int(input(">"))
    print("Enter the loan interest:")
    percent = float(input(">"))/100
    i = percent/(12*1)
    payment = (i * principal*math.pow(i+1, period)/ (math.pow(i+1, period)-1))
    payment = math.ceil(payment)
    print(f"Your monthly payment = {int(payment)}!")


elif type == "p":
    print("Enter the annuity payment:")
    payment = float(input(">"))
    print("Enter the number of periods:")
    period = int(input(">"))
    print("Enter the loan interest:")
    percent = float(input(">"))/100
    i = percent/(12*1)
    principal = - (payment-payment*math.pow(i+1, period))/(i*math.pow(i+1, period))
    principal = math.floor(principal)
    print(f"Your loan principal = {int(principal)}!")