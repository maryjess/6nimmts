from random import randint

def set_up_cards(cards):
	# returns a list containing the card decks.
	# card format is [number, cattle]

	NUM_OF_CARDS = 105
	# setting up the cards
	for i in range(1, NUM_OF_CARDS):
		curr_card = [i]
		if i % 5 == 0:
			if i % 10 == 0: 
				# 3 cattles
				curr_card.append(3)	
			elif i % 11 == 0: 
				# 7 cattles oops
				curr_card.append(7)
			else: 
				# two cattles
				curr_card.append(2)
			
		elif i % 11 == 0:
			# 5 cattles
			curr_card.append(5)
		else:
			curr_card.append(1)
		cards.append(curr_card)
	# print(cards)
	return cards

def distribute_cards(num_of_players, cards):
	# returns dictionary of each player 1 to num_of_players,
	# with values of a list containing the cards they have in hand
	players = {}
	smallest_index = 0
	largest_index = len(cards) - 1
	for j in range(num_of_players):
		j += 1
		if j not in players:
			players[j] = []
		for k in range(10):
			index = randint(smallest_index, largest_index)
			# print(smallest_index, largest_index)
			curr_card = cards[index]
			cards.pop(index)
			largest_index -= 1
			players[j].append(curr_card)
	print("sanity check for number of cards returned:", len(cards) == 104 - num_of_players * 10) # sanity check
	return [players, cards]

def set_up_decks(cards, deck):
	NUM_OF_COLS = 5
	NUM_OF_ROWS = 4
	# setting up empty deck
	deck = [[[0, 0] for i in range(NUM_OF_COLS)] for j in range(NUM_OF_ROWS)]

	smallest_index = 0
	largest_index = len(cards) - 1
	initial_cards = []
	for i in range(4):
		index = randint(smallest_index, largest_index)
		curr_card = cards[index]
		cards.pop(index)
		largest_index -= 1
		initial_cards.append(curr_card)
	initial_cards.sort(key = lambda x: x[0])idle
	for j, card in enumerate(initial_cards):
		deck[j][0] = card

	print(deck)
	return [deck, cards]

def is_row_full(row):
	if row[4] != [0, 0]:
		return True

cards = []
deck = []
cards = set_up_cards(cards)
# print(cards)
players, cards = distribute_cards(4, cards)
# print(players)
deck, cards = set_up_decks(cards, deck)
input("Please type the card that you would like to place: ")