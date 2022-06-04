import random


print('***** Arithmetic Test *****')
first_number = random.randint(2, 9)
second_number = random.randint(2, 9)
operator = random.choice(['+', '-', '*'])
answer = 0


def checking():
    if operator == '+':
        print(first_number + second_number)
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number


print(first_number, operator, second_number)
user_input = int(input('Write your answer: '))


def output():
    if user_input == checking():
        print("Right!")
    else:
        print("Wrong!")


output()
