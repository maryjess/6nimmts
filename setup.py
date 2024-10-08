from random import randint

#better to create a function that can select one card from the cards randomly
def pick_from_cards(cards):
    number_of_cards = len(cards)
    card_index = randint(0, number_of_cards - 1)
    card = cards.pop(card_index)
    return [cards, card] #your function can return more than one value without using array

def set_up_cards():
    cards = []
    for card_number in range(1, 104 + 1): #number of cards = 104
    #below is the optimized version of set_up_cards
        if card_number % 55 == 0:
            cards.append([card_number, 7])
        elif card_number % 11 == 0:
            cards.append([card_number, 5])
        elif card_number % 10 == 0:
            cards.append([card_number, 3])
        elif card_number % 5 == 0:
            cards.append([card_number, 2])
        else:
            cards.append([card_number, 1])
    return cards

def distribute_cards(num_of_players, cards):
    #below is the optimized version of distribute_cards
    players = {}
    for player in range(1, num_of_players + 1):
        if player not in players:
            players[player] = []
        for _ in range(10):
            cards, card = pick_from_cards(cards)
            players[player].append(card)
    return [players, cards]

def set_up_decks(cards, deck):
    #below is the optimized version of set_up_decks
    num_of_rows = 4
    deck = [[[0, 0] for _ in range(5)] for _ in range(4)] 
        # make a 4x5 array/matrix of [0, 0], the first card will be selected down below
        #although, i suggest making the deck [[], [], [], []] for simpler code, 
        #but the rest of the code in gameplay.py needed to be adjusted
        #also, why does the initial_cards needed to be sorted?
    initial_cards = [[0, 0] for _ in range(4)]
    for index in range(num_of_rows):
        cards, initial_cards[index] = pick_from_cards(cards)
    initial_cards.sort(key=lambda x: x[0])
    for index, card in enumerate(initial_cards):
        deck[index][0] = card
    return [deck, cards]

#the make_new_row can be erased and the functionality can be replaced by pick_from_cards(cards)