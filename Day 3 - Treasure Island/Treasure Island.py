#PART 1: BMI calculator:

height = float(input("enter height in m: "))
weight = float(input("enter yout weight in kg: "))

BMI = round(weight // height**2)
print("BMI = ", BMI)
if BMI <= 18.5:
    print("underweight")
elif BMI > 18.5 and BMI <=25:
    print("normal weight")
elif BMI > 25 and BMI <= 30:
    print("overweight")
elif BMI > 30 and BMI <= 35:
    print("obese")
else:
    print("clinically obese")

#PART 2: Check if year is a leap yesr (366 days)

year = int(input("Which year do you want to check?"))

flag = False

if year % 4 == 0:
    flag = True
    if year % 100 == 0:
        flag = True
        if year % 400 == 0:
            flag = True
        else:
            flag = False
    else:
        flag = False
else:
    flag = False

if flag == True:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

#PART 3 - Love Calculator
name1 = input("What is your name:\n")
name2 = input("What is your crush name:\n")

full_name = name1+name2
full_name = full_name.lower()

number1 = full_name.count("t") + full_name.count("r") + full_name.count("u") + full_name.count("e")
number2 = full_name.count("l") + full_name.count("o") + full_name.count("v") + full_name.count("e")

score = int(str(number1)+str(number2))

if score <= 10 and score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}, try another")


#PART 4 - Final Project
print("=========== Final Project - Treasure Island")

print("Welcome to treasure Island.\nYour misssion is to find the tresure.")

flag = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.\n")

if flag.lower() == 'right':
    print("Game OVER")
else:
    flag = input("You arrive at a lake full of sharks. Do you 'swim' or 'wait' for a boat.\n")
    if flag.lower() == 'swim':
        print("Game OVER")
    else:
        flag = input("You arrive at the destination. Choose one of the 3 doors: 'red', 'blue', yellow'.\n")
        if flag.lower() == 'red':
            print("Game OVER")
        elif flag.lower() == 'blue':
            print("Game OVER")
        elif flag.lower() == 'yellow':
            print("You WIN!")
        else:
            print("Wrong door color!")
            
    
            
