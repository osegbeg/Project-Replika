import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_maker = MoneyMachine()
my_menu = Menu()

# print(Menu.get_items(my_menu))
is_on = True

while is_on:
    choice = input(f"What would you like? {my_menu.get_items()}:  ")

    if choice == "off":
        sys.exit()
    elif choice == "report":
        my_coffee_maker.report()
        my_money_maker.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_maker.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)

