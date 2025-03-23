import random
print("Welcome to the Number Guessing Game!")\

print("I am thinking of a number between 1 and 100.")
number = random.randint(1, 100)

guess = input("Choose a difficulty. Type 'easy' for 10 attempts or 'hard' for 5 attempts:")

if guess == 'hard':
    nr_guess = 5
elif guess == 'easy':
    nr_guess = 10
else:
    raise ValueError('Wrong input!')

def check_number(nr):
    while nr > 0:
        print(f'You have {nr} attempts remaining to guess the number.')
        player_guess = int(input('Make a guess: '))
        nr -= 1
        if player_guess > number:
            print("Too high")
        elif player_guess < number:
            print("Too low")
        else:
            print(f"Your guess is right! Number is {number}")
            return

        if nr == 0:
            print(f"Game OVER! You did not guess the number! Number was: {number}")

check_number(nr=nr_guess)