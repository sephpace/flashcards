"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

import random

from deck import Deck


START_MSG = '\nType "exit" or "quit" to exit, ' \
            'type "hint" for a hint, ' \
            'or type "skip" to skip a question.\n'


class Quizzer:
    """
    Creates and manages a quizzing session.  Asks the user for the answer
    associated with the presented definition and validates their results.

    Incorrect answers are shuffled back into the deck once the game has ended.

    Attributes:
        deck (Deck):            The deck of cards for quizzing.
        discard (list of Card): The list of incorrect cards to be requizzed.
    """

    def __init__(self, deck_path):
        """
        Constructor.

        Args:
            deck_path (str): The path to a deck file to quiz on.
        """
        self.deck = Deck()
        self.deck.load(deck_path)
        self.deck.shuffle()
        self.discard = []


    def start(self):
        """
        Start the quizzing session. Sessions continue until the user manually
        quits or until they have answered every question correctly.
        """
        print(START_MSG)
        keep_quizzing = True
        while keep_quizzing:
            keep_quizzing = self.quiz()
            if len(self.discard) > 0:
                # Shuffle the discard pile
                random.shuffle(self.discard)

                # Add the discard pile back into the deck
                self.deck.add_all(self.discard)
                self.discard = []
            else:
                keep_quizzing = False
        print("Finished!")


    def quiz(self):
        """
        Quizzes the user on a single pass of each card in the deck.

        Returns:
            (bool): True if quizzing should continue and False otherwise.
        """
        # Quiz each card in the deck
        keep_quizzing = False
        while len(self.deck) > 0:
            # Display deck status
            remaining = len(self.deck) + len(self.discard)
            print("Remaining flash cards:", remaining, "\n")

            # Display the top card to the user
            card = self.deck.draw()
            print(f"\nWhat is this? --> {card.definition}\n")
            answer = input("Answer: ")

            # Parse user input
            if answer.lower() == "exit" or answer.lower() == "quit":
                # Stop quizzing
                keep_quizzing = False
                break
            elif answer.lower() == "hint":
                # Display the hint
                if card.hint is not None:
                    print(f"\nHint: {card.hint}\n")
                else:
                    print("\nNo hint available.\n")

                # Return the card to the deck
                self.deck.add(card)
            elif answer.lower() == "skip":
                # Skip the current card
                print()
            elif card.check_answer(answer):
                # Correct answer
                print("Correct!\n")
                print(card.get_formatted_answers())
            else:
                # Incorrect answer
                print("Incorrect!\n")
                print(card.get_formatted_answers())
                self.discard.append(card)
                keep_quizzing = True

        # Return the quiz result
        return keep_quizzing
