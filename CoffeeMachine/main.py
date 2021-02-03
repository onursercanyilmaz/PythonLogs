from data import *

def coffee_machine():
    flag = True

    while (flag == True):
        answer = input(">>> What would you like to drink? ").lower()

        if (answer == "espresso"):
            """do"""
            ingredients("espresso")
            change = askMoney() - menu["espresso"]["cost"]

            if (change > 0):

                print("Your change: " + str(change))
            else:
                print("Your money is not enough!")


        elif (answer == "latte"):
            """do"""

            ingredients("latte")
            change = askMoney() - menu["latte"]["cost"]

            if (change > 0):

                print("Your change: " + str(change))
            else:
                print("Your money is not enough!")

        elif (answer == "cappuccino"):
            """do"""

            ingredients("cappuccino")
            change = askMoney() - menu["cappuccino"]["cost"]

            if (change > 0):

                print("Your change: " + str(change))
            else:
                print("Your money is not enough!")

        elif (answer == "report"):
            """do"""
            ingredients("report")
        else:
            """do"""
            print("There is not like that drink!")


def askMoney():
    quarters = int(input("How many quarters: "))*0.25
    dimes = int(input("How many dimes: ")) *0.1
    nickles = int(input("How many nickles: "))*0.05
    pennies = int(input("How many pennies: "))*0.01
    total = quarters+dimes+nickles+pennies
    return total

def ingredients(coffee):
    machine_water = resources["water"]
    machine_coffee = resources["coffee"]
    machine_milk= resources["milk"]
    if(coffee =="espresso"):
        """do"""
        water = menu["espresso"]["ingredients"]["water"]
        coffee = menu["espresso"]["ingredients"]["coffee"]
        print("Water: " + str(water) + " ml\nCoffee: " + str(coffee) + " g")

        if (water > machine_water):
            """do"""
            print("There is no enough water!")
            coffee_machine()
        elif(coffee > machine_coffee):
            print("There is no enough coffee!")
            coffee_machine()
        else:
            resources["water"] = resources["water"] - water
            resources["coffee"] = resources["coffee"] - coffee



    elif(coffee=="latte"):
        """do"""
        water = menu["latte"]["ingredients"]["water"]
        coffee = menu["latte"]["ingredients"]["coffee"]
        milk = menu["latte"]["ingredients"]["milk"]
        print("Water: "+str(water)+" ml\nCoffee: "+str(coffee)+" g\nMilk: "+str(milk)+" ml")

        if (water > machine_water):
            """do"""
            print("There is no enough water!")
            coffee_machine()
        elif (coffee > machine_coffee):
            print("There is no enough coffee!")
            coffee_machine()
        elif (coffee > machine_milk):
            print("There is no enough milk!")
            coffee_machine()

        else:
            resources["water"] = resources["water"] - water
            resources["coffbreakee"] = resources["coffee"] - coffee
            resources["milk"] = resources["milk"] - milk

    elif(coffee=="cappuccino"):
        """do"""
        water = menu["cappuccino"]["ingredients"]["water"]
        coffee = menu["cappuccino"]["ingredients"]["coffee"]
        milk = menu["cappuccino"]["ingredients"]["milk"]
        print("Water: " + str(water) + " ml\nCoffee: " + str(coffee) + " g\nMilk: " + str(milk) + " ml")

        if (water > machine_water):
            """do"""
            print("There is no enough water!")
            coffee_machine()
        elif (coffee > machine_coffee):
            print("There is no enough coffee!")
            coffee_machine()
        elif (coffee > machine_milk):
            print("There is no enough milk!")
            coffee_machine()
        else:
            resources["water"] = resources["water"] - water
            resources["coffee"] = resources["coffee"] - coffee
            resources["milk"] = resources["milk"] - milk


    elif (coffee == "report"):
        print("Water: " + str(resources["water"]) + " ml\nCoffee: " + str(resources["coffee"] ) + " g\nMilk: " + str(resources["milk"] ) + " ml")



    else:
        """do"""
        print("There is not like that drink!")


print("Menu:\n☕ Espresso $1.5\n☕ Latte $2.5\n☕ Cappuccino $3.0")
coffee_machine()



