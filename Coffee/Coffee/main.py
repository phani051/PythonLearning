MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            'milk': 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 2. Check resources sufficient

def check_resources(drink):
    req_water = MENU[drink]['ingredients']['water']
    req_milk = MENU[drink]['ingredients']['milk']
    req_coffee = MENU[drink]['ingredients']['coffee']

    avail_water = resources['water']
    avail_milk = resources['milk']
    avail_coffee = resources['coffee']

    if avail_milk >= req_milk and avail_coffee >= req_coffee and avail_water >= req_water:
        return True
    elif avail_milk < req_milk:
        return "Milk"
    elif avail_coffee < req_coffee:
        return "Coffee"
    elif avail_water < req_water:
        return "Water"


# TODO 1. Print report of all resources
on = True
profit = 0
while on:
    command = input("What would you like? (espresso/latte/cappuccino): ")

    if command == 'report':
        for i, v in resources.items():
            print(f"{i}: {v}")
        print(f"Money: {profit}")
        continue
    if command == 'off':
        on = False
    else:
        # print(check_resources(command))
        req_resource = check_resources(command)
        # TODO 3. Process coins
        if check_resources(command) == True:
            quarters = int(input("Number of quarter coins: "))
            dimes = int(input("Number of dimes coins: "))
            nickles = int(input("Number of nickles coins: "))
            pennies = int(input("Number of pennies coins: "))
            money_inserted = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            print(f"Money inserted: {money_inserted}")
            # TODO 4. Check transaction successful?
            drink_cost = MENU[command]['cost']
            print(f"Drink cost {drink_cost}")
            if money_inserted < drink_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif money_inserted >= drink_cost:
                change = round(money_inserted - drink_cost, 3)
                print(f"Here is {change} in change.")
                profit += drink_cost
                # TODO 5. Make the coffee and deduct the resources.

                resources['water'] = resources['water'] - MENU[command]['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU[command]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU[command]['ingredients']['coffee']
                print(f"Here is your {command}. Enjoy!")

        else:
            print(f"There is no enough resources of {req_resource}")


