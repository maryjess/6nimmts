def place_card(players, player, card, deck):
    num_of_rows = 4
    num_of_cols = 5
    empty_card = [0, 0]

    if card not in players[player]:
        print("Error: The card you inputted is not in your hand! Please retype the card that you would like to place: ")
        return

    players[player].remove(card)
    to_place = card
    to_place_index = 0
    placed = False

    for j in range(num_of_rows):
        if deck[j][num_of_cols - 1] == empty_card:
            if deck[j][0][0] < card[0] and deck[j][to_place_index][0] < card[0]:
                to_place = card
                to_place_index = j

    for j in range(num_of_cols - 1):
        if not placed:
            if deck[to_place_index][j] == empty_card:
                deck[to_place_index][j] = card
                placed = True
            if j == num_of_cols - 2:
                for k in range(num_of_cols - 1):
                    deck[to_place_index][k] = empty_card
                deck[to_place_index][0] = card
                players[player].append(deck[to_place_index][j])

    return players, deck

def parse_card(card):
    card = card.strip('][').split(', ')
    if len(card) != 2:
        raise CardParseError("Invalid card format")
    try:
        card = [int(card[0]), int(card[1])]
    except ValueError:
        raise CardParseError("Card number or cattle count is not an integer")
    return card

def check_card_in_hand(card, cards):
    if card not in cards:
        raise CardNotInHandException("Card not in hand")


def ask_play_again():
    play_again = input("Would you like to play again? Type Yes or No: ")
    if play_again == "Yes":
        difficulty = input("Which difficulty you would like to play? Type Easy or Normal: ")
        from simulate import simulate
        simulate(difficulty)
    else:
        print("Thanks for playing! Hope to see you again.")
        exit()
