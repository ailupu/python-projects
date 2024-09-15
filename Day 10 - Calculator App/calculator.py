def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

first_nb = float(input('What\'s the first number?: '))
new_number = 0
flag = 'y'
while flag.lower() == 'y':
    print('+\n-\n*\n/\n')
    operation = input('Pick an operation: ')
    
    second_nb = float(input('What\'s the second number?: '))

    if operation == '+':
        new_number = add(first_nb, second_nb)
    elif operation == '-':
        new_number = substract(first_nb, second_nb)
    elif operation == '*':
        new_number = multiply(first_nb, second_nb)
    elif operation == '/':
        new_number = divide(first_nb, second_nb)
    else:
        print('UNKNOWN OPERATION!')
        break

    print(f'{first_nb} {operation} {second_nb} = {new_number}')

    new_operation = input(f'Type "y" to continue calculating with {new_number} or type "n" to start a new calculation. To close type "q": ')

    if new_operation.lower() == 'q':
        flag = new_operation.lower()
    elif new_operation.lower() == 'n':
        first_nb = float(input('What\'s the first number?: '))
        continue
    elif new_operation.lower() == 'y':
        first_nb = new_number
    else:
        print(f'Wrong input: {new_operation}')
        break




    
    

