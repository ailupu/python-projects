flag = 'yes'
action = {}
while flag.lower() == 'yes':
    name = input('What is your name: ')
    bid = int(input('What\'s your bid?: $'))

    action[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if more_bidders.lower() == 'yes':
        print(100*'\n')

    else:
        maximum = max(action, key=lambda key: action[key])
        print(f'Winner {maximum} with ${action[maximum]}')
        flag = more_bidders.lower()

