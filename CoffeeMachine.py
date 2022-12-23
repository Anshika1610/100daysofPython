MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "money": 0,
}

def money(quarters,dimes,nickles,pennies):
    total=quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total

is_machine_on=True
while is_machine_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if choice == 'Off':
        is_machine_on=False
    if choice == 'Report':
        print(f'Water : {resources["water"]}ml\nMilk : {resources["milk"]}ml\nCoffee : {resources["coffee"]}g\nMoney : ${resources["money"]}')
    if choice == 'Espresso':
        if resources["water"]>=MENU["espresso"]["ingredients"]["water"] and resources["coffee"]>=MENU["espresso"]["ingredients"]["coffee"]:
            print("Please insert the coins.")
            quarters=int(input("How many quarters?: "))
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))
            if money(quarters, dimes, nickles, pennies)>=MENU["espresso"]["cost"]:
                change=(money(quarters, dimes, nickles, pennies)-MENU["espresso"]["cost"])
                change=round(change,2)
                if money(quarters, dimes, nickles, pennies)==MENU["espresso"]["cost"]:
                    print("Here is your Espresso. Enjoy!")
                else :
                    print(f"Here is ${change} in change.\nHere is Espresso. Enjoy!")
                resources["water"]-= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
                resources["money"]+=MENU["espresso"]["cost"]
            else:
                print("Sorry the money was insufficient. Money refunded.")
        else:
            if resources["water"]<MENU["espresso"]["ingredients"]["water"]:
                if resources["coffee"]<MENU["espresso"]["ingredients"]["coffee"]:
                    print("Sorry. Not enough coffee and water.")
                else:
                    print("Sorry. Not enough water.")
            else:
                print("Sorry. Not enough coffee.")




    elif choice == 'Latte':
        if resources["water"]>=MENU["latte"]["ingredients"]["water"] and resources["coffee"]>=MENU["latte"]["ingredients"]["coffee"] and resources["milk"]>=MENU["latte"]["ingredients"]["milk"]:
            print("Please insert the coins.")
            quarters=int(input("How many quarters?: "))
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))
            if money(quarters, dimes, nickles, pennies)>=MENU["latte"]["cost"]:
                change=(money(quarters, dimes, nickles, pennies)-MENU["latte"]["cost"])
                change=round(change,2)
                if money(quarters, dimes, nickles, pennies)==MENU["latte"]["cost"]:
                    print("Here is your Latte. Enjoy!")
                else :
                    print(f"Here is ${change} in change.\nHere is Latte. Enjoy!")
                resources["water"]-= MENU["latte"]["ingredients"]["water"]
                resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
                resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
                resources["money"]+=MENU["latte"]["cost"]
            else:
                print("Sorry the money was insufficient. Money refunded.")
        else:
            if resources["water"]<MENU["latte"]["ingredients"]["water"]:
                if resources["coffee"]<MENU["latte"]["ingredients"]["coffee"]:
                    if resources["milk"]<MENU["latte"]["ingredients"]["milk"]:
                        print("Sorry. Not enough coffee, water and milk.")
                    else:
                        print("Sorry. Not enough coffee and water.")
                else:
                    if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                        print("Sorry. Not enough water and milk.")
                    else:
                        print("Sorry. Not enough water.")

            elif resources["coffee"]<MENU["latte"]["ingredients"]["coffee"]:
                if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                    print("Sorry. Not enough coffee and milk.")
                else:
                    print("Sorry. Not enough coffee.")

            elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                print("Sorry. Not enough milk.")




    elif choice == 'Cappuccino':
        if resources["water"]>=MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"]>=MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"]>=MENU["cappuccino"]["ingredients"]["milk"]:
            print("Please insert the coins.")
            quarters=int(input("How many quarters?: "))
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))
            if money(quarters, dimes, nickles, pennies)>=MENU["cappuccino"]["cost"]:
                change=(money(quarters, dimes, nickles, pennies)-MENU["cappuccino"]["cost"])
                change=round(change,2)
                if money(quarters, dimes, nickles, pennies)==MENU["cappuccino"]["cost"]:
                    print("Here is your Cappuccino. Enjoy!")
                else :
                    print(f"Here is ${change} in change.\nHere is Cappuccino. Enjoy!")
                resources["water"]-= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]
                resources["money"]+=MENU["cappuccino"]["cost"]
            else:
                print("Sorry the money was insufficient. Money refunded.")
        else:
            if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                    if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                        print("Sorry. Not enough coffee, water and milk.")
                    else:
                        print("Sorry. Not enough coffee and water.")
                else:
                    if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                        print("Sorry. Not enough water and milk.")
                    else:
                        print("Sorry. Not enough water.")

            elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                    print("Sorry. Not enough coffee and milk.")
                else:
                    print("Sorry. Not enough coffee.")

            elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry. Not enough milk.")

    


