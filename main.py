"""
Author: Seph Pace
Email:  sephpace@gmail.com
"""

import sys

from quiz import Quizzer


if __name__ == '__main__':
    source = sys.argv[1]
    quizzer = Quizzer(source)
    quizzer.start()
