# 6 nimmt! Game

**6 nimmt**! (also known as Take 6) is a popular card game designed by Wolfgang Kramer in 1994. It's played with a custom deck of 104 cards numbered 1-104, each bearing 1, 2, 3, 5, or 7 cattle heads that represent penalty points. Players aim to collect the fewest cattle heads by strategically placing cards on four rows according to simple rules. When a player places the sixth card in a row, they must take that entire row, scoring all the penalty points on those cards. 

The game ends when a player reaches 66 penalty points, and the player with the lowest total score wins. This fast-paced game combines strategic thinking with elements of luck, making it engaging for players of all ages

## Table of Contents
- [6 Nimmt! Game](#6-nimmt-game)
  - [Table of Contents](#table-of-contents)
  - [Game Setup](#game-setup)
  - [Gameplay](#gameplay)
  - [Project Structure](#project-structure)
  - [Functions](#functions)
    - [print_deck(deck)](#print_deckdeck)
    - [print_players(players)](#print_playersplayers)
    - [set_up_cards(cards)](#set_up_cardscards)
    - [distribute_cards(num_of_players, cards)](#distribute_cardsnum_of_players-cards)
    - [find_largest_cards_in_row(row)](#find_largest_cards_in_rowrow)
    - [set_up_decks(cards, deck)](#set_up_deckscards-deck)
    - [place_card(players, player, card, deck)](#place_cardplayers-player-card-deck)
    - [make_new_row(first_card)](#make_new_rowfirst_card)
    - [place_single_card(row, card)](#place_single_cardrow-card)
    - [is_row_full(row)](#is_row_fullrow)
    - [is_larger_card(curr_card, compared_card)](#is_larger_cardcurr_card-compared_card)
    - [determine_winners(players)](#determine_winnersplayers)
    - [parse_card(card)](#parse_cardcard)
    - [check_card_in_hand(card, current_deck)](#check_card_in_handcard-current_deck)
    - [play_game()](#play_game)
    - [simulate_debug()](#simulate_debug)
    - [simulate(difficulty)](#simulatedifficulty)
    - [ask_play_again()](#ask_play_again)

## Game Setup

- **Cards:** There are 105 cards, each with a unique number and a certain number of cattle heads (which are penalty points you want to avoid).
  - Cards that can be divided by 5 have 2 cattle heads, but if they can also be divided by 10, they have 3 cattle heads.
  - Cards that can be divided by 11 have either 5 or 7 cattle heads, making them more risky.
- **Decks:** 4 rows (decks) each capable of holding up to 5 cards.
- **Players:** 2-10 players. The goal is to avoid collecting penalty points.

## Gameplay

1. **Distribute Cards:** Each player is given 10 cards at the start.
2. **Setup Decks:** Initialize the 4 rows with a card.
3. **Player Turns:** 
   - Each player selects a card to place on the table.
   - The cards are then placed in rows according to their value.
   - If a player's card is smaller than any card in a row, they must take all cards in that row and place their card in a new row.
   - If a row is full, the player who places the next card takes the row.
4. **Determine Winner:** The game ends after 10 turns. The player with the fewest penalty points (cattle heads) wins.

## Project Structure

- **Main Python Script:** `main.py`
  - Implements the core game mechanics.
  - Contains the setup, distribution, gameplay, and winner determination logic.

## Functions

| Function                            | Description                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| `print_deck(deck)`                  | Prints the current deck situation.                                                           |
| `print_players(players)`            | Prints the cards held by each player.                                                        |
| `set_up_cards(cards)`               | Creates a list of 105 cards with varying cattle heads as penalty points.                     |
| `distribute_cards(num_of_players, cards)` | Distributes 10 cards to each player.                                                   |
| `find_largest_cards_in_row(row)`    | Finds the largest card in a row, helping to determine placement.                             |
| `set_up_decks(cards, deck)`         | Initializes the 4 rows of decks with cards.                                                  |
| `place_card(players, player, card, deck)` | Places a player's card into a row, handling cases like row overflow or invalid placement. |
| `make_new_row(first_card)`          | Creates a new row starting with a specific card.                                             |
| `place_single_card(row, card)`      | Places a single card into a specific row.                                                    |
| `is_row_full(row)`                  | Checks if a row is full.                                                                     |
| `is_larger_card(curr_card, compared_card)` | Compares two cards to determine which is larger.                                      |
| `determine_winners(players)`        | Calculates and announces the winner based on penalty points.                                 |
| `parse_card(card)`                  | Parses a card input by the player.                                                           |
| `check_card_in_hand(card, current_deck)` | Verifies that a card is in the player's hand.                                           |
| `play_game()`                       | Main function to start and manage the game.                                                  |
| `simulate_debug()`                  | Runs a debug simulation of the game.                                                         |
| `simulate(difficulty)`              | Runs the game with a specific difficulty level.                                              |
| `ask_play_again()`                  | Prompts the player to play again.                                                            |



## How to Play

1. Clone the repository.
```bash
git clone https://github.com/maryjess/6nimmts.git
```
2. Run the `main.py` file.
3. Follow the on-screen instructions to play the game.

## License

This project is open-source and licensed under the MIT License.
