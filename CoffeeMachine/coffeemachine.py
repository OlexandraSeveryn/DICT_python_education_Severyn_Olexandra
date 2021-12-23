print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

STATE_COMMAND = 0
STATE_BUY = 1
STATE_FILL_1 = 2
STATE_FILL_2 = 3
STATE_FILL_3 = 4
STATE_FILL_4 = 5
STATE_FILL_5 = 6


class CoffeeMachine:
    available_water = 400
    available_milk = 540
    available_beans = 15
    available_money = 550
    available_cup = 9
    exit = False
    state = STATE_COMMAND
    action = ""
    type_coffee = ""

    def __init__(self):
        self.reset()

    def printStatus(self):
        print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        {} of money""".format(self.available_water,
                              self.available_milk,
                              self.available_beans,
                              self.available_cup,
                              self.available_money))

    def reset(self):
        self.state = STATE_COMMAND
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def input(self, text):
        global add_cups
        if self.state == STATE_COMMAND:
            self.action = text

            if self.action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
                self.state = STATE_BUY

            elif self.action == "fill":
                print("Write how many ml of water you want to add:")
                self.state = STATE_FILL_1

            elif self.action == "take":
                print("I gave you {}".format(self.available_money))
                self.available_money = 0
                self.reset()

            elif self.action == "remaining":
                self.printStatus()
                self.reset()

            elif self.action == "exit":
                self.exit = True
                self.state = STATE_COMMAND

        elif self.state == STATE_BUY:
            self.type_coffee = text

            if self.type_coffee == "back":
                self.reset()
                return
            else:
                type_coffee = int(self.type_coffee)

            coffee_max = min(self.available_water // 200, self.available_milk // 50, self.available_beans // 15)

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

            if water <= self.available_water and milk <= self.available_milk and beans <= self.available_beans:

                if coffee_max == 1:
                    print("Yes, I can make that amount of coffee")
                elif coffee_max > 1:
                    print("Yes, I can make that amount of coffee (and even {} more than that)".format(
                        coffee_max - 1))

                self.available_money += price

            else:
                print("No, I can make only {} cups of coffee".format(coffee_max))

            self.reset()

        elif self.state == STATE_FILL_1:
            add_water = int(text)
            self.available_water += add_water

            print("Write how many ml of milk you want to add:")
            self.state = STATE_FILL_2

        elif self.state == STATE_FILL_2:
            add_milk = int(text)
            self.available_milk += add_milk

            print("Write how many grams of coffee beans you want to add:")
            self.state = STATE_FILL_3

        elif self.state == STATE_FILL_3:
            add_beans = int(text)
            self.available_beans += add_beans

            print("Write how many disposable coffee cups you want to add:")
            self.state = STATE_FILL_4

        elif self.state == STATE_FILL_4:
            add_cups = int(text)
            self.available_cup += add_cups

            self.reset()


coffeeMachine = CoffeeMachine()

while True:
    text = input(">")
    coffeeMachine.input(text)

    if coffeeMachine.exit:
        break