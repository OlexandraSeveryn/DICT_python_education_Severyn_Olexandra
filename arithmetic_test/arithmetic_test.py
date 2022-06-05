import random
import operator

print('***** Arithmetic Test *****')
print('Which level do you want?')


def level():
    lvl = ['1 - Simple operations with numbers 2-9', '2 - Integral squares of 11-29']
    print(lvl[0])
    print(lvl[1])


def users_input():
    user_input = int(input('Enter a number:'))
    while user_input > 2 or user_input <= 0:
        print('Incorrect format!')
        user_input = int(input('Try again:'))
    else:
        return user_input


def checking():
    if users_input() == 1:
        oper = {'+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv}
        first_number = random.randint(2, 9)
        second_number = random.randint(2, 9)
        operate = random.choice(list(oper.keys()))
        answer = oper.get(operate)(first_number, second_number)
        print('{} {} {}'.format(first_number, operate, second_number))
        return answer

    elif users_input() == 2:
        integr_square = random.randint(11, 29)
        answer2 = integr_square ** 2
        print('{}'.format(integr_square))
        return answer2


def proverka():
    while True:
        try:
            answer = checking()
            user_input = int(input('Write your answer: '))
            return user_input == answer
        except ValueError:
            print('Incorrect input!')


def output():
    mark = 0
    for i in range(5):
        correct = proverka()
        if correct:
            mark += 1
            print("Right!")
        else:
            print("Wrong!")

    print('Your mark is {}/5.'.format(mark))

    print('Would you like to save the result? Enter yes or no.')
    yes_no = input('>>>')
    if yes_no == 'yes':
        print("What is your name?")
        name = input()
        file = open('results.txt', '+w')
        file.write(name + f' Yor mark is: {mark}/5')
        print('The results are saved in "results.txt".')


level()
output()
