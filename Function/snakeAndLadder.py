import random
import time
from datetime import datetime
from itertools import cycle
from tkinter.ttk import Frame

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from Function.player import *


class snakeAndLadder:
    """
        function:
            addPlayer(): add a new player to this game, store it in array self.player[]
            move(): make the current player move their step
        variable:
            self.player[]: store all player object into array
            self.snakes{}: store all snakes into this dict
            self.ladders{} store all ladders into this dict
            self.current_player: store the next player object
        """
    def __init__(self):
        self.current_player = None
        self.players = []
        self.snakes = {99: 69, 91: 61, 87: 57, 65: 52, 47: 19, 34: 1, 25: 5}
        self.ladders = {69: 98, 63: 95, 3: 51, 36: 55, 20: 70, 6: 27}

    def addPlayer(self, player_list):
        # add player object into player list
        for i in player_list:
            # judge weather it has robot
            if not i == "":
                self.players.append(player(i))
            else:
                self.players.append(player("robot"+"-"+str(datetime.now().time())))

        for i in self.players:
            print(i.name)

        # define the first player
        pool = cycle(self.players)
        self.current_player = pool.__next__()

    def move(self,event):
        self.current_player.dice()
        self.current_player.current_position += self.current_player.number
        if not self.current_player.isGameEnd():
            # judge if the player trigger the snakes or the ladders
            if self.current_player.current_position in self.snakes.keys():
                self.current_player.current_position = self.snakes[self.current_player.current_position]
                print("snakes!!! back to {}".format(self.current_player.current_position))
            if self.current_player.current_position in self.ladders.keys():
                print("ladders!!! Going to {}".format(self.current_player.current_position))
            print("you are now in position {}".format(self.current_player.current_position))
        else:
            return "game is over"



