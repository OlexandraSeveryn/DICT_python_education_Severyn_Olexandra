import random

x = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
name = str(input("enter your name"))
print(f"Hello: {name}")
point = 0
r = open('rating.txt', 'r')
for context in r:
    nick, score = context.split()
    if name == nick:
        point = int(score)

while True:
    cmp = random.choice([*x.keys()])
    pl = str(input(""))
    if pl == "rating":
        print(f"your score: {point}")
    if pl == "exit":
        print("Bye")
        break
    if pl == cmp:
        print("Draw")
        point += 50
        continue
    elif pl == x.get(cmp):
        print(f"Sorry, but the computer chose {cmp}")
        continue
    elif x.get(pl) == cmp:
        print(f"Well done. The computer chose {cmp} and failed")
        point += 100
        continue
    else:
        print("Choose the item!")
        continue
