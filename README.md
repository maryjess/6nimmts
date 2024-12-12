# Welcome to 6nimmts! 🍻
This project is a digital version of the card game **6 nimmt**! (also known as Take 6),
designed by Wolfgang Kramer in 1994. 

# (Mini) Developer's Guide

## Project Structure

- Main Python Script is located at `main.py`
  - Implements the core game mechanics.
  - Contains the setup, distribution, gameplay, and winner determination logic.

## Table of Functions

| Function                                   | Input(s)                                       | Description                                                                               |
|--------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------|
| `print_deck()`                             | `deck`                                         | Prints the current deck situation.                                                        |
| `print_players()`                          | `players`                                      | Prints the cards held by each player.                                                     |
| `set_up_cards()`                      | `cards`                                        | Creates a list of 105 cards with varying cattle heads as penalty points.                  |
| `distribute_cards()`  | `num_of_players, cards`                        | Distributes 10 cards to each player.                                                      |
| `find_largest_cards_in_row()`           | `row`                                          | Finds the largest card in a row, helping to determine placement.                          |
| `set_up_decks()`                | `cards, deck`                                  | Initializes the 4 rows of decks with cards.                                               |
| `place_card()`  | `players, player, card, deck`                  | Places a player's card into a row, handling cases like row overflow or invalid placement. |
| `make_new_row()`                 | `first_card`                                   | Creates a new row starting with a specific card.                                          |
| `place_single_card()`             | `row, card`                                    | Places a single card into a specific row.                                                 |
| `is_row_full()`                         | `row`                                          | Checks if a row is full.                                                                  |
| `is_larger_card()` | `curr_card, compared_card`                     | Compares two cards to determine which is larger.                                          |
| `determine_winners()`               | `players`                                      | Calculates and announces the winner based on penalty points.                              |
| `parse_card()`                         | `card`                                         | Parses a card input by the player.                                                        |
| `check_card_in_hand()`   | `card, current_deck`                           | Verifies that a card is in the player's hand.                                             |
| `play_game()`                              | `-`                                            | Main function to start and manage the game.                                               |
| `simulate_debug()`                         | `-`| Runs a debug simulation of the game.                                                      |
| `simulate()`                     | `difficulty`| Runs the game with a specific difficulty level.                                           |
| `ask_play_again()`                         | `-`| Prompts the player to play again.                                                         |

## How to Play

1. Clone the repository.
```bash
git clone https://github.com/maryjess/6nimmts.git
```
2. Run the `main.py` file.
3. Follow the on-screen instructions to play the game.
