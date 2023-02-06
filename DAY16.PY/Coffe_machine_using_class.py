from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Money_machine = MoneyMachine()
Coffe_maker = CoffeeMaker()
menu = Menu()


is_on = True


while is_on:
    options = menu.get_items()
    order = input(f"what would you like ? ({options})")
    if order == "off":
        is_on = False
    elif order == "report":
        Money_machine.report()
        Coffe_maker.report()
    else:
        drink = menu.find_drink(order)
        if Coffe_maker.is_resource_sufficient(drink) and Money_machine.make_payment(drink.cost):
            Coffe_maker.make_coffee(drink)
        
        