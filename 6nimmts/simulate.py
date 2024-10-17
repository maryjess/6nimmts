from setup import set_up_cards, distribute_cards, set_up_decks
from utils import place_card, parse_card, check_card_in_hand, ask_play_again
from printing import print_deck, print_players
from exceptions import InvalidRowNumberException, CardNotInHandException, CardParseError #exception has been imported
from random import randint

def simulate_debug():
    win_condition = False
    cards = []
    deck = [[[13, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[14, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[23, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[87, 1], [0, 0], [0, 0], [0, 0], [0, 0]]]
    cards = set_up_cards(cards)
    players, cards = distribute_cards(4, cards)
    players[1] = [[32, 1], [96, 1], [45, 2], [23, 1], [17, 1], [56, 1], [3, 1], [85, 2], [11, 5]]

    print_deck(deck)
    print_players(players)

    for _ in range(3):
        print("Here are your cards:", players[1])
        cards_to_place = []
        for i in range(4):
            if len(players[i + 1]) == 0:
                print(f"Player {i + 1} wins! Congratulations.")
                win_condition = True
                break
            if i == 0:
                print("Your turn")
            else:
                print(f"Player {i + 1}'s turn")
            cards = players[i+1]
            if i == 0:
                card = input("(Type in format, [<number>, <cattle>]): ")
                try:
                    card = parse_card(card)
                    check_card_in_hand(card, cards)
                except CardParseError:
                    card = input("The card format you've entered is invalid. Please enter the card again:")
                except CardNotInHandException:
                    card = input("Error: The card you inputted is not in your hand! Please retype the card that you would like to place: ")
            else:
                cards.sort(key=lambda x:x[0])
                cards.sort(key=lambda x:x[1], reverse=True)
                card = cards[0]
            cards_to_place.append((card, i))
        if win_condition:
            break
        cards_to_place.sort(key=lambda x: x[0][0])
        for c, p in cards_to_place:
            players, deck = place_card(players, p + 1, c, deck)
            print('---')
            print_deck(deck)
        print('---')
        print("end of turn")
        print_deck(deck)
    if win_condition:
        print("Thanks for playing!")
        exit()
    print('===')
    print("final deck condition:")
    print_deck(deck)
    print("---")
    print("final players condition:")
    print_players(players)
    print("calculating winner...")
    print(determine_winners(players))
    ask_play_again()

def simulate(difficulty):
    #with the old code, if the user enter incorrect difficulty for the second time, 
    #the code will continue to set up card with incorrect difficulty
    correct_input = False
    difficulty = 'NA'
    while correct_input == False:
        if difficulty not in ['Easy', 'Normal']:
            difficulty = input("The difficulty you've entered is invalid! Please either enter Easy or Normal: ")
        else:
            correct_input = True

    win_condition = False
    #do not create cards here, its better to cards=[] in setup.set_up_cards()
    #do not create cards here, its better to deck=[] in setup.set_up_decks()
    cards = set_up_cards(cards)
    players, cards = distribute_cards(4, cards)
    deck, cards = set_up_decks(cards, deck)
    print_deck(deck)

    for _ in range(10):
        print("Here are your cards:", players[1])
        cards_to_place = []
        for i in range(4):
            if len(players[i + 1]) == 0:
                print(f"Player {i + 1} wins! Congratulations.")
                win_condition = True
                break
            if i == 0:
                print("Your turn")
            else:
                print(f"Player {i + 1}'s turn")
            cards = players[i+1]
            if i == 0:
                card = input("(Type in format, [<number>, <cattle>]): ")
                try:
                    card = parse_card(card)
                    check_card_in_hand(card, cards)
                except CardParseError:
                    card = input("The card format you've entered is invalid. Please enter the card again:")
                except CardNotInHandException:
                    card = input("Error: The card you inputted is not in your hand! Please retype the card that you would like to place: ")
            else:
                if difficulty == 'Easy':
                    card = cards[randint(0, len(cards) - 1)]
                else:
                    cards.sort(key=lambda x:x[0])
                    cards.sort(key=lambda x:x[1], reverse=True)
                    card = cards[0]
            cards_to_place.append((card, i))
        if win_condition:
            break
        cards_to_place.sort(key=lambda x: x[0][0])
        for c, p in cards_to_place:
            players, deck = place_card(players, p + 1, c, deck)
            print('---')
            print_deck(deck)
        print('---')
        print("end of turn")
        print_deck(deck)
    if win_condition:
        ask_play_again()
    print('===')
    print("final deck condition:")
    print_deck(deck)
    print("---")
    print("calculating winner...")
    print(determine_winners(players))
    ask_play_again()

def determine_winners(players):
    current_winner = None
    winning_penalty = 0
    for p, cards in players.items():
        current_penalty = 0
        for c in cards:
            current_penalty += c[1]
        if winning_penalty > current_penalty:
            winning_penalty = current_penalty
            current_winner = p

    #havent consider tie
    if current_winner is not None:
        return f'The winner is Player {current_winner}! Congratulations.'
    else:
        return f'No winner could be determined.'
