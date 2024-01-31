# 1 - Heads or Tails
import random

random_number = random.randint(0,1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")

# 2 - Banker Roulette

people = "A, B, C, D, E"
list_people = people.split(", ")
random_number = random.randint(0, len(list_people)-1)

print(f"{list_people[random_number]} will pay the bill")

# 3 - Treasure Map
line1 = ["A","B","C"]
line2 = ["A","B","C"]
line3 = ["A","B","C"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

index_list = int(position[-1]) - 1

if position[0] in map[index_list]:
    map[index_list][map[index_list].index(position[0])] = "X"

print(f'{line1}\n{line2}\n{line3}')