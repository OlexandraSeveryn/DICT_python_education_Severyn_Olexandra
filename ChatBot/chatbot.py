def welcome():
    print("Hello! My name is Bob_Bot")
    print("I was created in 2021")
    name=input("Please, remaind me your name:")
    print("What a great name you have,", name)

def age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3=int(input())
    remainder5=int(input())
    remainder7=int(input())
    age_guest=(remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print("Yor age is:" + str(age_guest) + "That's a good time to start programming!")

def play():
    print("Now I will prove to you that I can count to any number you want.")
    number=int(input())
    for i in range(number + 1):
        print(str(i)+"!")


def game():
    print("Let's test your programming knowledge.")
    print("What is an algoritm?")
    print("1. It's a process of performing calculations that lead to the solution of the problem.")
    print("2. It's a pecifying to perform actions.")
    print("3. It's a system of rules that describes the sequence of actions that must be performed to solve the problem.")
    x=0
    while x !=2:
        x=int(input())
        if x==2:
            print("Completed, have a nice day!")
        else:
            print("Please, try again.")


print("Congratulations, have a nice day!")

welcome()
age()
play()
game()