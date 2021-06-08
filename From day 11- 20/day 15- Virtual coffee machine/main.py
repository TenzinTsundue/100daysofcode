# virtual coffee machine
# where you enter which coffee you want, enter the amount and get the coffee
# you can check you resources with report and turn off the machine with off command

# importing resource form resource file. menu, resources and money
import resource as rs


# process coins
def check_coins(item):
    # How many quarters dime nickles pennies
    quarter = int(input("Number of quarter: ")) * .25
    dime = int(input("Number of dime: ")) * .10
    nickle = int(input("Number of nickles: ")) * .05
    pennie = int(input("Number of pennies: ")) * .01
    total_input = quarter + dime + nickle + pennie
    total_cost = rs.menu[item]["cost"]
    if total_input < total_cost:
        print(f'insufficient amount, Returning deposit ... ')
    elif total_input > total_cost:
        print(f'Here is {total_input - total_cost} in change')
        return True
    else:
        return True


# print report
def report():
    print(f"water: {rs.resources['water']}")
    print(f"Milk: {rs.resources['milk']}")
    print(f"Coffee: {rs.resources['coffee']}")
    print(f"Money: {rs.money}")


# check resource sufficient?
def check_resource(item):
    if rs.menu[item]["ingredients"]["water"] > rs.resources["water"] or \
            rs.menu[item]["ingredients"]["milk"] > rs.resources["milk"] or\
            rs.menu[item]["ingredients"]["coffee"] > rs.resources["coffee"]:
        print("No sufficient resource, try other coffee")


# make coffee
def make_coffee(item):
    # check_coins(item)
    # check_resource(item)
    if check_coins(item) and check_resource(item):
        rs.resources["water"] = rs.resources["water"] - rs.menu[item]["ingredients"]["water"]
        rs.resources["milk"] = rs.resources["milk"] - rs.menu[item]["ingredients"]["milk"]
        rs.resources["coffee"] = rs.resources["coffee"] - rs.menu[item]["ingredients"]["coffee"]
        rs.money = rs.money + rs.menu[item]["cost"]
        print(f'{item} made, Enjoy!')


# print(resource.menu["espresso"]["ingredients"]["water"])
# WHat would you like? (espresso/latte/cappuccino): report/off
machine = True
while machine:
    command = input("What would you like? Espresso(1), Latte(2), Cappuccino(3): ")
    if command == 'report':
        report()
    elif command == '1':
        make_coffee("espresso")
    elif command == '2':
        make_coffee("latte")
    elif command == '3':
        make_coffee("cappuccino")
    elif command == 'off':
        machine = False
    else:
        print("Incorrect input, 1 for Espresso, 2 for Latte and 3 for Cappuccino")


