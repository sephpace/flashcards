
import random

import Card

class Deck:
    """Constructor"""
    def __init__(self, source_file):

        # Create cards from source file
        self.__cards = []

        read_line = False
        with open(source_file) as note_file:
            for line in note_file:
                # Look for the marker to start reading the flash cards
                if "%%%" in line:
                    if read_line:
                        read_line = False
                    else:
                        read_line = True
                    continue

                if read_line:
                    split_line = line.split(":")
                    split_line[0] = split_line[0].split(",")
                    for i in range(len(split_line[0])):
                        split_line[0][i] = split_line[0][i].lstrip()
                        split_line[1].lstrip()
                    if len(split_line) == 3:
                        split_line[2].lstrip()
                        self.__cards.append(Card.Card(split_line[0], split_line[1], split_line[2]))
                    elif len(split_line) == 2:
                        self.__cards.append(Card.Card(split_line[0], split_line[1]))

    """Getters"""
    def get_card_count(self):
        return len(self.__cards)

    def get_card(self, index=0):
        return self.__cards[index]

    """Shuffles the deck"""
    def shuffle(self):
        random.shuffle(self.__cards)

    """Removes card from the deck at the given index"""
    def remove_card(self, index):
        self.__cards.pop(index)

    """Removes the given card from the deck"""
    def remove_card(self, card):
        self.__cards.pop(self.__cards.index(card))

    """Adds the given card to the list"""
    def add_card(self, card):
        self.__cards.append(card)