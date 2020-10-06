"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

import sys

from deck import Deck


if __name__ == '__main__':
    source = sys.argv[1]

    flash_cards = []

    # Create deck
    deck = Deck(source)

    # Start quizzing
    deck.shuffle()

    print("\nType \"exit\" or \"quit\" to exit, type \"hint\" for a hint, or type \"skip\" to skip a question.\n")

    while len(deck) > 0:
        print("Remaining flash cards:", len(deck), "\n")

        card = deck.draw()
        card.print_definition()
        answer = input("Answer: ")

        # Check if the answer is a command or actually an answer
        if answer.lower() == "exit" or answer.lower() == "quit":
            sys.exit()
        elif answer.lower() == "hint":
            card.print_hint()
            deck.add(card)
        elif answer.lower() == "skip":
            print()
        else:
            if card.check_answer(answer):
                print("Correct!")
                card.print_answer()
            else:
                print("Incorrect!")
                card.print_answer()
                deck.add(card)

    print("Finished!")
