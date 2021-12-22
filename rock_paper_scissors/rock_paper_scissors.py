while True:
    x = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
    t = str(input(""))
    y = x.get(t)
    if t in x:
        print(f"Sorry, but the computer chose {y}")
    else:
        print("Choose the item!")
        continue
