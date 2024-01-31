import random
your_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

input_list = ["Rock","Paper", "Scissors"]

computer_input = random.randint(0,2)

if your_input == computer_input:
    print("You choose '{}', computer choose '{}'. It's a tie!".format(input_list[your_input],input_list[computer_input]))

elif computer_input > your_input:
    print("You choose '{}', computer choose '{}'. COMPUTER WINS!".format(input_list[your_input],input_list[computer_input]))

elif your_input == 0 and computer_input == 2:
    print("You choose '{}', computer choose '{}'. YOU WIN!".format(input_list[your_input],input_list[computer_input]))

elif your_input > computer_input :
     print("You choose '{}', computer choose '{}'.YOU WIN!".format(input_list[your_input],input_list[computer_input]))

elif your_input == 2 and computer_input == 0:
    print("You choose '{}', computer choose '{}'. COMPUTER WINS!".format(input_list[your_input],input_list[computer_input]))

else:
    print("Invalid INPUT! Please try again!")