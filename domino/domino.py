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
print(f"Stock pieces {[slice_stock]}")
print(f"Player pieces {[slice_player]}")
print(f"Computer pieces {[slice_computer]}")
print(f"Domino snake {m}")
if len(slice_computer) > len(slice_player):
    print("Status: Computer")
elif len(slice_player) > len(slice_computer):
    print("Status: Player")
