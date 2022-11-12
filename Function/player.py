import random
from tkinter.ttk import Frame

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class player:
    """
    function:
        dice(): give a random number between 1 and 6, store number in self.number
    variable:
        current_position: the current position of this player
    """

    def __init__(self, name):
        self.name = name
        self.number = 0
        self.current_position = 0
        self.is_robot = False

    def dice(self):
        self.number = random.randint(1, 6)

    def isGameEnd(self):
        if self.current_position == 100:
            return True
        # we must ensure the position is accurately equal to 100
        if self.current_position >= 100:
            self.current_position -= self.number
            print("You roll a dice greater than 100, back to the previous position: {}".format(self.current_position))
