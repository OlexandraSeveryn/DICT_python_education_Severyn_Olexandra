import random

domino_pieces = [[x, y] for x in range(0, 7) for y in range(0, 7) if x >= y]
random.shuffle(domino_pieces)
slice_stock = domino_pieces[:14]
slice_player = domino_pieces[21:28]
slice_computer = domino_pieces[14:21]
tier_list = []
while True:
    for i in slice_player:
        if i == i[::-1]:
            tier_list.append(i)
    for i in slice_computer:
        if i == i[::-1]:
            tier_list.append(i)
    if len(tier_list) >= 1:
        break
    else:
        pass
if len(tier_list) > 1:
    m = max(tier_list)
else:
    m = tier_list
if m in slice_player:
    slice_player.remove(m)
    choice = "Status: Computer is about to make a move. Press Enter to continue..."
else:
    slice_computer.remove(m)
    choice = "Status: It's your turn to make a move. Enter your command. "
tier_list = [m]


def interface(m):
    print("=" * 70)
    print(f"""Stock pieces {len(slice_stock)}
Computer pieces {len(slice_computer)}
If you don't have a suitable dominance press 0 and you get 1 domino.
""")
    if len(m) <= 6:
        print(m)
    elif len(m) > 6:
        print(f"""{m[:3]}...{m[-3:]}""")
    print("""
Your pieces:
       """)
    for x, item in enumerate(slice_player):
        print(f"{x + 1}: {item}")


def check():
    while True:
        player_answer = input("Status: It's your turn to make a move. Enter your command. ")
        try:
            int(player_answer)
            if int(player_answer) not in range(-len(slice_player), len(slice_player) + 1):
                print("you don't have that much")
                continue
            else:
                return player_answer
        except ValueError:
            print("Invalid input. Please try again.")
            continue


def player_input():
    turn = False
    player_answer = int(check())
    while not turn:
        if player_answer < 0:
            if slice_player[abs(player_answer) - 1][-1] == tier_list[0][0]:
                tier_list.insert(0, slice_player[-player_answer - 1])
                slice_player.remove(slice_player[-player_answer - 1])
                turn = True
            elif slice_player[abs(player_answer) - 1][0] == tier_list[0][0]:
                tier_list.insert(0, slice_player[-player_answer - 1][::-1])
                slice_player.remove(slice_player[-player_answer - 1])
                turn = True
            else:
                print("wrong one")
                player_answer = int(check())
        elif player_answer > 0:
            if slice_player[player_answer - 1][0] == tier_list[-1][1]:
                tier_list.append(slice_player[player_answer - 1])
                slice_player.remove(slice_player[player_answer - 1])
                turn = True
            elif slice_player[player_answer - 1][1] == tier_list[-1][1]:
                tier_list.append(slice_player[player_answer - 1][::-1])
                slice_player.remove(slice_player[player_answer - 1])
                turn = True
            else:
                print("wrong one")
                player_answer = int(check())
        elif player_answer == 0:
            slice_player.append(slice_stock[0])
            del slice_stock[0]
            turn = True
        else:
            print("Incorrect input. Enter number ")
            continue


def computer_input():
    turn = False
    while not turn:
        computer_answer = random.choice(range(-len(slice_computer), len(slice_computer) + 1))
        if computer_answer < 0:
            if slice_computer[abs(computer_answer) - 1][-1] == tier_list[0][0]:
                tier_list.insert(0, slice_computer[abs(computer_answer) - 1])
                slice_computer.remove(slice_computer[abs(computer_answer) - 1])
                turn = True
            elif slice_computer[abs(computer_answer) - 1][0] == tier_list[0][0]:
                tier_list.insert(0, slice_computer[abs(computer_answer) - 1][::-1])
                slice_computer.remove(slice_computer[abs(computer_answer) - 1])
                turn = True
        elif computer_answer > 0:
            if slice_computer[computer_answer - 1][0] == tier_list[-1][1]:
                tier_list.append(slice_computer[computer_answer - 1])
                slice_computer.remove(slice_computer[computer_answer - 1])
                turn = True
            elif slice_computer[computer_answer - 1][1] == tier_list[-1][1]:
                tier_list.append(slice_computer[computer_answer - 1][::-1])
                slice_computer.remove(slice_computer[computer_answer - 1])
                turn = True
        else:
            slice_computer.append(slice_stock[0])
            del slice_stock[0]
            turn = True


interface(tier_list)

while True:
    if len(slice_computer) > 0 and len(slice_player) > 0:
        if choice == "Status: Computer is about to make a move. Press Enter to continue...":
            print(input("Status: Computer is about to make a move. Press Enter to continue..."))
            computer_input()
            choice = "Status: It's your turn to make a move. Enter your command"
        else:
            player_input()
            choice = "Status: Computer is about to make a move. Press Enter to continue..."
    interface(tier_list)
    if len(slice_player) == 0:
        print("""The game is over. You won!
            You have 0 pieces""")
        break
    elif len(slice_computer) == 0:
        print("The game is over. The computer won!")
        break
    elif tier_list[0][0] == tier_list[-1][-1]:
        score = 0
        for i in range(len(tier_list)):
            for s in tier_list[i]:
                if s == tier_list[0][0]:
                    score += 1
        if score == 8:
            print("The game is over. It's a draw!")
            break
    elif len(slice_stock) == 0:
        if choice == "Status: Computer is about to make a move. Press Enter to continue...":
            print("The game is over. You won!")
            break
        elif choice == "Status: It's your turn to make a move. Enter your command":
            print("The game is over. The computer won!")
            break
