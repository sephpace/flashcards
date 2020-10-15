"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

import random

import yaml

from card import Card

class Deck:
    """
    A deck contains one or more cards.

    Attributes:
        __cards (list of Card): The cards in the deck.
    """

    def __init__(self, cards=None):
        """
        Constructor.

        Args:
            cards (list of Card): The cards to add to the deck. Optional.
        """
        self.__cards = cards if cards is not None else []


    def __len__(self):
        return len(self.__cards)


    def add(self, card):
        """
        Adds a card to the top of the deck.

        Args:
            card (Card): The card to add to the deck.
        """
        self.__cards.append(card)


    def add_all(self, cards):
        """
        Adds all of the given cards to the top of the deck.

        Args:
            cards (list of Card): The cards to add to the deck.
        """
        self.__cards.extend(cards)


    def draw(self):
        """
        Draws a card from the deck.

        The card will be removed once drawn unless manually added back in

        Returns:
            (Card): The card from the top of the deck.
        """
        return self.__cards.pop()


    def load(self, path):
        """
        Loads a deck from the deck file at the given path.

        Args:
            path (str): The path to the deck file to load.
        """
        # Extract information from the deck file
        with open(path, 'r') as file:
            info = yaml.safe_load(file.read())

        # Create cards with the extracted information
        cards = []
        for card_info in info['cards']:
            cards.append(Card(**card_info))

        # Add the cards to the deck and remove old ones
        self.__init__(cards)


    def save(self, path):
        """
        Saves the deck to the file at the given path.

        Args:
            path (str): The path to save the deck file to.
        """
        # Set up deck information
        info = {
            'cards': []
        }

        # Gather the card information
        for card in self.__cards:
            info['cards'].append({
                'answers': card.answers,
                'definition': card.definition,
                'hint': card.hint,
            })

        # Save to a deck file
        with open(path, 'w') as file:
            file.write(yaml.safe_dump(info))


    def shuffle(self):
        """
        Shuffles the cards in the deck.
        """
        random.shuffle(self.__cards)
