import sys
import random

import Deck
import Card

source = sys.argv[1]

flash_cards = []

# Create deck
deck = Deck.Deck(source)

# Start quizzing
deck.shuffle()

print("\nType \"exit\" or \"quit\" to exit, type \"hint\" for a hint, or type \"skip\" to skip a question.\n")

while(deck.get_card_count() > 0):
    print("Remaining flash cards:", deck.get_card_count(), "\n")

    card = deck.get_card()
    card.print_definition()
    answer = input("Answer: ")

    # Check if the answer is a command or actually an answer
    if answer.lower() == "exit" or answer.lower() == "quit":
        sys.exit()
    elif answer.lower() == "hint":
        card.print_hint()
    elif answer.lower() == "skip":
        print()
        deck.remove_card(card)
    else:
        if card.is_correct(answer):
            print("Correct!")
            card.print_answer()
            deck.remove_card(card)
        else:
            print("Incorrect!")
            card.print_answer()
            deck.remove_card(card)
            deck.add_card(card)

print("Finished!")