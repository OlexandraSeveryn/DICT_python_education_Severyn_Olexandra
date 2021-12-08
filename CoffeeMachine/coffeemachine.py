print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")



print("Write how many ml of water the coffee machine has:")
available_water = int(input(">"))
print("Write how many ml of milk the coffee machine has:")
available_milk = int(input(">"))
print("Write how many grams of coffee beans the coffee machine has:")
available_beans = int(input(">"))

coffee_max = min(available_water//200, available_milk//50, available_beans//15)

print("Write how many cups of coffee you will need:")
cups = int(input(">"))

water = 200*cups
milk = 50*cups
beans = 15*cups

if water<= available_water and milk <= available_milk and beans<= available_beans:

    if coffee_max == 1:
        print("Yes, I can make that amount of coffee")
    elif coffee_max > cups:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(coffee_max-cups))
else:
    print("No, I can make only {} cups of coffee".format(coffee_max))

print("""For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans""".format(cups, 200*cups, 50*cups, 15*cups))
