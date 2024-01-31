# Average Height

student_heights = list(map(int, input("Student heights:").split()))

number_students = 0
total_height = 0

for height in student_heights:
    number_students += 1
    total_height += height

print("Total height: {}". format(total_height))
print("Number of students:", number_students)
print("Average height of the class is: {}".format(round(total_height/number_students)))



# High Score
ex = [78, 65, 89, 86, 55, 91, 64, 89]

score = list(map(int, input("Scores: ").split()))

max_nr = 0
for el in score:
    if el > max_nr:
        max_nr = el
print("The heighest score in the class is: {}".format(max_nr))



# Adding Even Numbers
all_numbers = int(input("Add number: "))

sum_even_nr = 0
for i in range(0,all_numbers+1):
    if i % 2 == 0:
        sum_even_nr += i

print(f"Sum of only even numbers for {all_numbers} is {sum_even_nr}")



#F FizzBuzz Game

number = int(input("Choose number for FizzBuzz: "))

for i in range(1,number+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 