from random import randint

def set_up_cards(cards):
    num_of_cards = 105
    for i in range(1, num_of_cards):
        curr_card = [i]
        if i % 5 == 0:
            if i % 10 == 0:
                curr_card.append(3)
            elif i % 11 == 0:
                curr_card.append(7)
            else:
                curr_card.append(2)
        elif i % 11 == 0:
            curr_card.append(5)
        else:
            curr_card.append(1)
        cards.append(curr_card)
    return cards

def distribute_cards(num_of_players, cards):
    players = {}
    smallest_index = 0
    largest_index = len(cards) - 1
    for j in range(num_of_players):
        j += 1
        if j not in players:
            players[j] = []
        for _ in range(10):
            index = randint(smallest_index, largest_index)
            curr_card = cards[index]
            cards.pop(index)
            largest_index -= 1
            players[j].append(curr_card)
    return [players, cards]

def set_up_decks(cards, deck):
    num_of_rows = 4
    deck = [make_new_row([0, 0]) for _ in range(num_of_rows)]
    smallest_index = 0
    largest_index = len(cards) - 1
    initial_cards = []
    for _ in range(num_of_rows):
        index = randint(smallest_index, largest_index)
        curr_card = cards[index]
        cards.pop(index)
        largest_index -= 1
        initial_cards.append(curr_card)
    initial_cards.sort(key=lambda x: x[0])
    for j, card in enumerate(initial_cards):
        deck[j][0] = card
    return [deck, cards]

def make_new_row(first_card):
    empty_card = [0, 0]
    return [first_card, empty_card, empty_card, empty_card, empty_card]
