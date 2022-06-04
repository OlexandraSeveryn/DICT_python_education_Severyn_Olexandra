import random
import operator

print('***** Arithmetic Test *****')


def checking():
    oper = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul}
    first_number = random.randint(2, 9)
    second_number = random.randint(2, 9)
    operate = random.choice(list(oper.keys()))
    answer = oper.get(operate)(first_number, second_number)
    print('{} {} {}'.format(first_number, operate, second_number))
    return answer


def proverka():
    answer = checking()
    user_input = int(input('Write your answer: '))
    return user_input == answer


def output():
    correct = proverka()
    if correct:
        print("Right!")
    else:
        print("Wrong!")


output()
