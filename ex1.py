#triunghi nr -> impare
# metoda primeste un nr -> randul din piramida => suma nr

def returnSum(lista1):
    return sum(lista1)

lista_numere = [[1], [3,5], [7,9,11], [13,15,17,19], [21,23,25,27,29]]

number_of_row = int(input("Write max numbers of rows: "))

number = 1

pyramid_list = list()

for i in range(1,number_of_row+1):
    pyramid_list.append([])
    for nr in range(1,i+1):
        if number %2 != 0:
            pyramid_list[i-1].append(number)
            print(number, end= " ")
        number +=2
    print("\r") 

sum_of_last_row = returnSum(pyramid_list[-1])
print("The sum of the numbers from the last row of pyramid is: ", sum_of_last_row)

"""
line_number = input("Write specific row: ")

list_to_be_added = list()

for row in range(len(lista_numere)):
    if row+1 == int(line_number):
        list_to_be_added = lista_numere[row]
        print(list_to_be_added)
        break

numbers_added = returnSum(list_to_be_added)

print(f"Sum of the elements from row {line_number} is {numbers_added}")

"""
