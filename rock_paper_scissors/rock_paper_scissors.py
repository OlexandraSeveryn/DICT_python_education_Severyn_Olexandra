import random
while True:
    x = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    pl = str(input(""))
    cmp = random.choice([*x.keys()])
    if pl == "exit":
        print("Bye")
        break
    if pl == cmp:
        print("Draw")
        continue
    elif pl == x.get(cmp):
        print(f"Sorry, but the computer chose {cmp}")
        continue
    elif x.get(pl) == cmp:
        print(f"Well done. The computer chose {cmp} and failed")
        continue
    else:
        print("Choose the item!")
        continue
