from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":
    startCoffee = True
    coffee = CoffeeMaker()
    moneyHandler = MoneyMachine()
    menu = Menu()
    while startCoffee:
        order = input("What would you like today?"
                      "(espresso/latte/cappuccino): ")
        if order == "report":
            coffee.report()
            moneyHandler.report()
        elif order == "exit":
            startCoffee = False
        else:
            order = menu.find_drink(order)
            if order and coffee.is_resource_sufficient(order) \
               and moneyHandler.make_payment(order.cost):
                coffee.make_coffee(order)
