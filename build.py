"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

from card import Card
from deck import Deck


def import_deck(source_path, out_path):
    """
    Parses the deck information from the text file at the given source.

    Args:
        source_path (str): The path to the source file.
        out_path (str):    The path for the resulting deck file.
    """
    # Parse the source file for deck information
    cards = []
    read_line = False
    with open(source_path) as file:
        for line in file.readlines():
            # Look for the marker to start reading the flash cards
            if "%%%" in line:
                read_line = not read_line
                continue

            # Extract definitions, answers, and hints from the given line
            if read_line:
                # Extract information
                info = line.split(':')
                answers = [answer.strip() for answer in info[0].split(',')]
                definition = info[1].strip()
                hint = info[2] if len(info) == 3 else None

                # Create the card and add to the cards list
                cards.append(Card(answers, definition, hint))

    # Create and save the deck
    deck = Deck(cards)
    deck.save(out_path)
