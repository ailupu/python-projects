#number = input("Write a 2 digit number: ")
#print("The digits added: ", (int(number[0])+int(number[1])))

print("==========  Your life in weeks ============")
age = input("Your age: ")
remaining_age = (90-int(age))
days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age *12
print(f"You have {days} days, {weeks} weeks, {months} months left.")

print("========== TIP Calculator =============")
print("Welcome to the Tip Calculator")
      
total = float(input("What is the total bill? $"))
      
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


new_tip = round(tip/100,2)
total_bill = total + total * new_tip

pay = round(total_bill/people,2)

print(f"Each person should pay: {pay}")
