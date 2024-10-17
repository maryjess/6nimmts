def print_deck(deck):
    for row in deck:
        print(row)

def print_players(players):
    for player, hand in players.items():
        print(f"Player {player}'s hand: {hand}")
