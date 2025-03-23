import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def random_number(list):
    return random.choice(list)

def starting_cards(list):
    return [random_number(list)]

def sum_of_cards(list_cards):
    total = sum(list_cards)
    aces = list_cards.count(11)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def players_turn(first_hand):
    sum_of_cards_player = sum_of_cards(first_hand)
    if sum_of_cards_player > 21:
        return "Sum more than 21. YOU LOST!"
    if sum_of_cards_player == 21:
        return "Sum is 21. YOU WIN!"
    
    game = input("Type 'y' to draw one more card; type 'n' to pass: ")
    while game == 'y':
        first_hand += starting_cards(cards)
        sum_of_cards_player = sum_of_cards(first_hand)
        print(f"New sum of cards: {sum_of_cards_player}")
        if sum_of_cards_player > 21:
            return "Sum more than 21. YOU LOST!"
        if sum_of_cards_player == 21:
            return "Sum is 21. YOU WIN!"
        game = input("Type 'y' to draw one more card; type 'n' to pass: ")

    return int(sum_of_cards_player)

def dealers_turn(first_hand):
    sum_cards_dealer = sum_of_cards(first_hand)
    while sum_cards_dealer < 17:
        first_hand += starting_cards(cards)
        sum_cards_dealer = sum_of_cards(first_hand)
    return int(sum_cards_dealer)

def closer_to_21(nr1, nr2):
    diff1 = abs(21 - nr1)
    diff2 = abs(21 - nr2)
    if diff1 < diff2:
        return f"Player: {nr1} wins!"
    elif diff2 < diff1:
        return f"Dealer: {nr2} wins!"
    else:
        return f"Both have {nr1}. It's a tie!"

# Game starts here
player_first_hand = starting_cards(cards) + starting_cards(cards)
dealer_first_hand = starting_cards(cards) + starting_cards(cards)

print(f"Your starting hand: {player_first_hand}. Total sum: {sum_of_cards(player_first_hand)}")
print(f"Computer's first card: {dealer_first_hand[0]}")
player_turn = players_turn(player_first_hand)
dealer_turn = dealers_turn(dealer_first_hand)

if isinstance(player_turn, int):
    if dealer_turn > 21 and player_turn <= 21:
        print(f"Dealer hand {dealer_turn}. YOU WIN!")
    elif dealer_turn == player_turn:
        print(f"DEALER: {dealer_turn}. PLAYER: {player_turn}. TIE!")
    else:
        print(closer_to_21(player_turn, dealer_turn))
else:
    print(player_turn)