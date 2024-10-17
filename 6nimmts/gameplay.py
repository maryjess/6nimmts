#from setup import set_up_cards, distribute_cards, set_up_decks #this is redundant

from simulate import simulate_debug, simulate

def play_game():
    try:
        print("Welcome to 6nimmts!") 
        mode = input("Which difficulty would you like to play? Please enter Easy or Normal: ")
        if mode == "Debug":
            simulate_debug()
        else:
            simulate(mode)
    except KeyboardInterrupt:
        print("Bye!")
        exit()
