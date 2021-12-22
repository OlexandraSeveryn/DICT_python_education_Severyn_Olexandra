import math
import sys


def getArgValue(nameArg):
    for i in range(1, len(sys.argv)):
        if sys.argv[i].startswith("--" + nameArg + "="):
            arg = sys.argv[i]
            return arg[arg.index("=") + 1:len(arg)]
    return None


def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def error():
    print("Incorrect parameters")
    exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        error()
    type = getArgValue("type")
    if not type in ["annuity", "diff"]:
        error()
    payment = getArgValue("payment")
    if payment and (not isNumber(payment) or int(payment) <= 0):
        error()
    if payment:
        payment = float(payment)

    principal = getArgValue("principal")
    if principal and (not isNumber(principal) or int(principal) <= 0):
        error()
    if principal:
        principal = float(principal)

    periods = getArgValue("periods")
    if periods and (not isNumber(periods) or int(periods) <= 0):
        error()
    if periods:
        periods = int(periods)

    interest = getArgValue("interest")
    if not periods or not isNumber(interest) or float(interest) <= 0:
        error()
    interest = float(interest) / 100

    if type == "diff":
        if not principal or not periods:
            error()

        i = interest / (12 * 1)
        sum = 0
        for m in range(1, periods + 1):
            diff = principal / periods + i * (principal - (principal * (m - 1)) / periods)
            diff = math.ceil(diff)
            print(f"Month {m}: payment is {diff}")
            sum += diff
        print(f"Overpayment = {int(sum - principal)}")

    elif type == "annuity":
        if principal and payment:
            i = interest / (12 * 1)

            n = math.log(payment / (payment - i * principal), 1.0 + i)
            n = math.ceil(n)
            year = n / 12
            if year % 1 > 0:
                month = (year % 1) * 12

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
            print(f"Overpayment = {int((n * payment) - principal)}")

        elif principal and periods:
            i = interest / (12 * 1)
            payment = (i * principal * math.pow(i + 1, periods) / (math.pow(i + 1, periods) - 1))
            payment = math.ceil(payment)
            print(f"Your monthly payment = {int(payment)}!")
            print(f"Overpayment = {int((periods * payment) - principal)}")

        elif payment and periods:
            i = interest / (12 * 1)
            principal = - (payment - payment * math.pow(i + 1, periods)) / (i * math.pow(i + 1, periods))
            principal = math.floor(principal)
            print(f"Your loan principal = {int(principal)}!")
            print(f"Overpayment = {int((periods * payment) - principal)}")