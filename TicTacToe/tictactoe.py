fill = input("Enter cells:")

print ("-"*5)
for y in range(3):
    print("|", end="")
    for x in range(3):
        print(fill[y*x],end="")
    print("|")
print ("-"*5)