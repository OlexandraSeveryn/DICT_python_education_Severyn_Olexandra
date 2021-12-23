import random

domino_pieces = [[x, y] for x in range(0, 7) for y in range(0, 7) if x >= y]
while True:
    random.shuffle(domino_pieces)
    slice_stock = domino_pieces[:14]
    slice_player = domino_pieces[21:28]
    slice_computer = domino_pieces[14:21]
    tier_list = []
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
elif m in slice_computer:
    slice_computer.remove(m)
print("-" * 70)
print(f"""Stock pieces {len(slice_stock)}
Computer pieces {len(slice_computer)}
{m}
Your pieces:
    """)
for i, item in enumerate(slice_player):
    print(f"{i + 1}: {item}")
print("")
if len(slice_computer) > len(slice_player):
    print("Status: Computer is about to make a move. Press Enter to continue...")
elif len(slice_computer) < len(slice_player):
    input("Status: It's your turn to make a move. Enter your command. ")