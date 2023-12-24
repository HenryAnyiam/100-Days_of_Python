#!/usr/bin/python3
"""Build a coffee machine imitator"""


def displayResources(resources, money):
    """Displays quantity of resources left"""
    for i in resources:
        print(f"{i.title()}: {resources[i]}", end="")
        if i == "coffee":
            print("g")
        else:
            print("ml")
    print(f"${money}")


def checkResources(menu, order, resources):
    """Checks that order can be made"""
    if order not in menu:
        return (False, "Order not in menu")
    ingredients = menu[order]['ingredients']
    left = {}
    for i in resources:
        left[i] = resources[i] - ingredients.get(i, 0)
        if left[i] < 0:
            return (False, f"Sorry there is not enough {i} left")
    return (True, left)


def checkMoney(order, menu):
    """Gets clients money"""
    print("Please insert coins")
    quarters = input("How many quaters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")
    try:
        total = 0.25 * int(quarters)
        total += 0.10 * int(dimes)
        total += 0.05 * int(nickels)
        total += 0.01 * int(pennies)
    except ValueError:
        return (False, "Coin not inserted correctly")
    else:
        cost = menu[order]['cost']
        change = round(total - cost, 2)
        if change < 0:
            return (False, "Insufficient coins given")
        elif change == 0:
            return (True, "You have no change", cost)
        return (True, f"Here is ${change} in change", cost)


def makeCoffee(menu, resources, money):
    """Starts the coffee maker"""
    startMachine = True
    while startMachine:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        order = order.lower()
        if order == "report":
            displayResources(resources, money)
        elif order == "exit":
            startMachine = False
        else:
            make = checkResources(menu, order, resources)
            if make[0] is False:
                print(make[1])
            else:
                cash = checkMoney(order, menu)
                print(cash[1])
                if cash[0] is True:
                    print(f"Here is your {order}")
                    resources = make[1]
                    money += cash[2]


if __name__ == "__main__":
    from data import MENU, resources
    money = 0
    makeCoffee(MENU, resources, money)
