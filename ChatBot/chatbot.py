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

