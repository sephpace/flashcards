"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

import argparse

from quiz import Quizzer
from build import import_deck


def build(source, output):
    """
    The build command. Parses a deck from a text file and saves
    the deck into a deck file in the given output location.

    Args:
        source (str): The path to the source text file to parse.
        output (str): The output deck file path.
    """
    import_deck(source, output)


def quiz(deck):
    """
    Start quizzing the user with the given deck file.

    Args:
        deck (str): The path to the deck file.
    """
    quizzer = Quizzer(deck)
    quizzer.start()


if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, choices=('build', 'quiz'),
                        help='The command to call')
    parser.add_argument('source', type=str, help='The source file')
    parser.add_argument('output', type=str, default='deck.yml', nargs='?',
                        help='The output file when building a deck')
    args = parser.parse_args()

    # Run a command based on the given args
    if args.command == 'build':
        build(args.source, args.output)
    elif args.command == 'quiz':
        quiz(args.source)
    else:
        parser.print_usage()
