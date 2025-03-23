MENU = {
    "espresso" : {
        "ingridients" : {
            "water" : 50,
            "coffee" : 18
        },
        "cost" : 1.5
    },
    "latte" : {
        "ingridients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 2.5
    },
    "cappuccino" : {
        "ingridients" : {
            "water" : 250,
            "milk" : 100,
            "coffee": 24
        },
        "cost" : 3.0
    }
}

machine_water = 300
machine_milk = 200
machine_coffee = 100
machine_money =  0

machine_working = True

def process_coins(quarters, dimes, nickles, pennies):
    dollars = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return dollars

def print_machine_report(water, milk, coffee, money):
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')

def check_coffee(action):
    try:
        if machine_water < MENU["action"]["ingridients"]["water"]:
            return False
        elif machine_coffee < MENU["action"]["ingridients"]["coffee"]:
            return False
        elif machine_milk < MENU["action"]["ingridients"]["milk"]:
            return False
        else:
            return True
    except:
        pass

def check_resources_depleyed():
    if machine_water == 0 or machine_coffee == 0 or machine_milk == 0:
        return False
    return True

def check_money(inserted_money, action):
    if inserted_money > MENU[action]["cost"]:
        returned_money = inserted_money - MENU[action]["cost"]
        print(f"Here is ${returned_money} dollars in change.")
    elif inserted_money < MENU[action]["cost"]:
        print("Sorry not enough money. Money refunded.")
        return False
    return True


while machine_working:
    action=input("What would you like? (espresso/latte/cappuccino (or report)): ")
    
    if not check_resources_depleyed():
        print("Resources depleyed! Machine turning off!")
        break

    elif action.lower() == "off":
        print("Coffee machine is turning off!")
        break

    elif action.lower() == "report":
        print_machine_report(machine_water, machine_milk, machine_coffee, machine_money)
        action=input("What would you like? (espresso/latte/cappuccino (or report)): ")
    
    else:
        flag = check_coffee(action)
        if flag == False:
            print(f"Not enough resources for {action}")
            break

    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    money_added = process_coins(quarters, dimes, nickles, pennies)
    checking_transaction = check_money(money_added, action)
    if not checking_transaction:
        pass
    else:
        machine_money += MENU[action]["cost"]

    machine_water -= MENU[action]["ingridients"]["water"]
    machine_coffee -= MENU[action]["ingridients"]["coffee"]
    if "milk" in MENU[action]["ingridients"]:
        machine_milk -= MENU[action]["ingridients"]["milk"]

    print("Here is your coffee! Enjoy!")