"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""


class Card:
    """
    A card contains a definition and a list of answers that correspond with it.

    Cards can optionally contain hints.

    Attributes:
        __answers (list of str): A list of possible answers for the card.
        __definition (str):      The question/definition for the card.
        __hint (str, optional):  The hint associated with the definition.
    """

    def __init__(self, answers, definition, hint=None):
        """
        Constructor.

        Args:
            answers (list of str): A list of possible answers for the card.
            definition (str):      The question/definition for the card.
            hint (str, optional):  The hint associated with the definition.
        """
        self.__answers = answers
        self.__definition = definition
        self.__hint = hint

    def check_answer(self, answer):
        """
        Determines if the given answer is correct.

        Args:
            answer (str): The answer to check.

        Returns:
            (bool): True if the answer is correct and false otherwise.
        """
        correct = False
        for ans in self.__answers:
            if answer.lower() == ans.lower():
                correct = True
        return correct

    def print_answer(self):
        """
        Displays the answer(s) of the card.
        """
        print("\nThe answer is ", end="")
        for i in range(len(self.__answers)):
            if i > 0:
                print(" or ", end="")
            print(f"\"{self.__answers[i]}\"", end="")
        print(".\n")

    def print_definition(self):
        """
        Displays the card definition.
        """
        print(f"\nWhat is this? --> {self.__definition}\n")

    def print_hint(self):
        """
        Displays the card hint, if available.
        """
        if self.__hint is not None:
            print(f"\nHint: {self.__hint}\n")
        else:
            print("\nNo hint available.\n")
