import random
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

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
lucky = input(">")
luckyman = ""
if lucky == "Yes":
    luckyman = random.choice(list(friends.keys()))
    print("{} is the lucky one!".format(luckyman))
    lucky = 1
else:
    print("No one is going to be lucky")
    lucky = 0

bill = round(amount/(numFriends-lucky), 2)

for key in friends:
    if luckyman != key :
        friends[key] = bill

print(friends)


