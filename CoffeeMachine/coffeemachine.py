print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

available_water = 400
available_milk = 540
available_beans = 15
available_money = 550
available_cup = 9


def printStatus():
    print("""The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    {} of money""".format(available_water, available_milk, available_beans, available_cup, available_money))

printStatus()

while True:

    print("Write action (buy, fill, take, remaining, exit):")
    action = input(">")

    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        type_coffee = input(">")

        if type_coffee == "back":
            continue
        else:
            type_coffee = int(type_coffee)

        coffee_max = min(available_water // 200, available_milk // 50, available_beans // 15)

        water = milk = beans = price = 0

        if type_coffee == 1:
            water = 250
            milk = 0
            beans = 16
            price = 4
        elif type_coffee == 2:
            water = 350
            milk = 75
            beans = 20
            price = 7
        elif type_coffee == 3:
            water = 200
            milk = 100
            beans = 12
            price = 6

        if water <= available_water and milk <= available_milk and beans <= available_beans:

            if coffee_max == 1:
                print("Yes, I can make that amount of coffee")
            elif coffee_max > 1:
                print("Yes, I can make that amount of coffee (and even {} more than that)".format(coffee_max - 1))

            available_money += price
            printStatus()

        else:
            print("No, I can make only {} cups of coffee".format(coffee_max))

    elif action =="fill":
        print("Write how many ml of water you want to add:")
        add_water = int(input(">"))
        print("Write how many ml of milk you want to add:")
        add_milk = int(input(">"))
        print("Write how many grams of coffee beans you want to add:")
        add_beans = int(input(">"))
        print("Write how many disposable coffee cups you want to add:")
        add_cups = int(input(">"))

        available_water += add_water
        available_milk += add_milk
        available_beans += add_beans
        available_cup += add_cups
        printStatus()
    elif action == "take":
        print("I gave you {}".format(available_money))
        availableMoney = 0
        printStatus()
    elif action == "remaining":
        printStatus()
    elif action == "exit":
        break