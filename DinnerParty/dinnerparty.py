print("Enter the number of friends joining (including you):")
numFriends = input(">")
if numFriends.isnumeric():
    numFriends = int(numFriends)
    if numFriends <= 0:
        print("No one is joining for the party")
        exit()
else:
    print("No one is joining for the party")
    exit()

friends = {}
for i in range(numFriends):
    print("Enter the name of every friend (including you), each on a new line:")
    name = input(">")
    friends[name] = 0

print("Enter the total amount:")
amount = int(input(">"))
bill = round(amount/numFriends, 2)
for key in friends:
    friends[key] = bill


print(friends)