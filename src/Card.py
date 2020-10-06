

class Card:
    """Constructor"""
    def __init__(self, answers, definition, hint=None):
        self.__answers = answers
        self.__definition = definition
        self.__hint = hint

    """Function to check if an answer is correct"""
    def is_correct(self, user_answer):
        correct = False
        for answer in self.__answers:
            if user_answer.lower() == answer.lower():
                correct = True
        return correct
    
    """Print functions"""
    def print_answer(self):
        print("\nThe answer is ", end="")
        for i in range(len(self.__answers)):
            if i > 0:
                print(" or ", end="")
            print(f"\"{self.__answers[i]}\"", end="")
        print(".\n")

    def print_definition(self):
        print(f"\nWhat is this? --> {self.__definition}\n")

    def print_hint(self):
        if self.__hint != None:
            print(f"\nHint: {self.__hint}\n")
        else:
            print("\nNo hint available.\n")