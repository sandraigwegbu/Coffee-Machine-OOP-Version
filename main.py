from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Run the coffee machine
coffee_machine_is_on = True
while coffee_machine_is_on:

	# User prompt
	options = menu.get_items()
	response = input(f"What drink would you like? ({options})): ").lower()

	# Turn off the coffee machine. Prompt is "off".
	# Print report that shows current values of [Water, Milk, Coffee, Money]. Prompt is "report".
	# Check resources sufficient.
	if response == "off":
		coffee_machine_is_on = False
	elif response == "report":
		money_machine.report()
		coffee_maker.report()
	else:
		drink = menu.find_drink(response)
		# Check that resources are sufficient, process coins & check that funds are sufficient
		if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
			# Make coffee
			coffee_maker.make_coffee(drink)

