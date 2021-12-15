fill = input("Enter cells:")

print ("-"*5)
for y in range(3):
    print("|", end="")
    for x in range(3):
        print(fill[y*3+x],end="")
    print("|")
print ("-"*5)

def win():

    win_side = ""

    for y in range(3):
        line = ""
        for x in range(3):
            line += fill[y*3+x]
        if line.count(line[0]) == 3:
            win_side += line[0]

    diag1 = ""
    diag2 = ""

    for x in range(3):
        line = ""
        for y in range(3):
            line += fill[y * 3 + x]
            if x == y:
                diag1 += fill[y * 3 + x]
            if x == 2-y:
                diag2 += fill[y * 3 + x]

        if line.count(line[0]) == 3:
            win_side += line[0]
        if diag1.count(diag1[0]) == 3:
            win_side += diag1[0]
        if diag2.count(diag2[0]) == 3:
            win_side += diag2[0]
    return win_side

if abs(fill.count("X")- fill.count("O")) > 1 or len(win())>1:
    print("Impossible")
else:
    if "_" in fill:
       if len(win()) == 1:
           print(win() + " wins")
       else :
           print("Game not finished")

    else:
        if len(win()) == 1:
            print(win() + " wins")
        else :
            print("Draw")