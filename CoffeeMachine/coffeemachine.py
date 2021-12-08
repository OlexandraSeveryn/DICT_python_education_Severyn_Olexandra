print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")
print("Write how many cups of coffee you will need:")
cups = int(input(">"))

print("""For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans""".format(cups, 200*cups, 50*cups, 15*cups))
