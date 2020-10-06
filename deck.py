"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

from queue import Queue
import random

from card import Card

class Deck:
    """
    A deck contains one or more cards.

    Attributes:
        __cards (list of Card): The cards in the deck.
    """

    def __init__(self, source):
        """
        Constructor.

        Args:
            source (str): The path to the deck source file.
        """
        # Create cards from source file
        self.__cards = Queue()

        read_line = False
        with open(source) as note_file:
            for line in note_file:
                # Look for the marker to start reading the flash cards
                if "%%%" in line:
                    read_line = not read_line
                    continue

                # Extract definitions, answers, and hints from the given line
                # TODO: Clean this up.  I wrote this when I was a programming
                # noob.  Either refactor or use YAML instead.
                if read_line:
                    split_line = line.split(":")
                    split_line[0] = split_line[0].split(",")
                    for i in range(len(split_line[0])):
                        split_line[0][i] = split_line[0][i].lstrip()
                        split_line[1].lstrip()
                    if len(split_line) == 3:
                        split_line[2].lstrip()
                        self.__cards.put(Card(split_line[0], split_line[1], split_line[2]))
                    elif len(split_line) == 2:
                        self.__cards.put(Card(split_line[0], split_line[1]))

    def __len__(self):
        return self.__cards.qsize()

    def add(self, card):
        """
        Adds a card onto the bottom of the deck.

        Args:
            card (Card): The card to add to the deck.
        """
        self.__cards.put(card)

    def draw(self):
        """
        Draws a card from the deck.

        The card will be removed once drawn unless manually added back in

        Returns:
            (Card): The card from the top of the deck.
        """
        return self.__cards.get()

    def shuffle(self):
        """
        Shuffles the cards in the deck.
        """
        # Extract cards from queue
        card_list = []
        while not self.__cards.empty():
            card_list.append(self.__cards.get())

        # Shuffle extracted cards
        random.shuffle(card_list)

        # Reinsert cards into queue
        for card in card_list:
            self.__cards.put(card)
