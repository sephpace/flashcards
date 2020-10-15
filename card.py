"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""


class Card:
    """
    A card contains a definition and a list of answers that correspond with it.

    Cards can optionally contain hints.

    Attributes:
        answers (list of str): A list of possible answers for the card.
        definition (str):      The question/definition for the card.
        hint (str, optional):  The hint associated with the definition.
    """

    def __init__(self, answers, definition, hint=None):
        """
        Constructor.

        Args:
            answers (list of str): A list of possible answers for the card.
            definition (str):      The question/definition for the card.
            hint (str, optional):  The hint associated with the definition.
        """
        self.answers = answers
        self.definition = definition
        self.hint = hint


    def check_answer(self, answer):
        """
        Determines if the given answer is correct.

        Args:
            answer (str): The answer to check.

        Returns:
            (bool): True if the answer is correct and false otherwise.
        """
        correct = False
        for ans in self.answers:
            if answer.lower() == ans.lower():
                correct = True
        return correct


    def get_formatted_answers(self):
        """
        Returns a formatted string containing the answers.

        Returns:
            (str): The formatted answers.
        """
        answers = ' or '.join(self.answers)
        return f'\nThe answer is {answers}.\n'
