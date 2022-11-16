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
            isGameEnd(): judge if current player reach at position 100, then end the game.
        variable:
            self.player[]: store all player object into array
            self.snakes{}: store all snakes into this dict
            self.ladders{} store all ladders into this dict
            self.current_player: store the next player object
            self.game_status: game is end when it is equal to 1, not end when equal to 0
        """

    def __init__(self):
        self.game_status = None
        self.current_player = None
        self.players = []
        self.snakes = {99: 69, 91: 61, 87: 57, 65: 52, 47: 19, 34: 1, 25: 5}
        self.ladders = {69: 98, 63: 95, 3: 51, 36: 55, 20: 70, 6: 27}
        self.pool = None

    def addPlayer(self, player_list):
        # add player object into player list
        if self.players == []:
            for i in player_list:
                # judge weather it is a robot
                if not i == "":
                    self.players.append(player(i))
                else:
                    robot = player("robot" + "-" + str(datetime.now().time()))
                    robot.is_robot = True
                    self.players.append(robot)

            for i in self.players:
                print(i.name)
        else:
            print("Please do not submit more than one time")

        # define the first player
        self.pool = cycle(self.players)
        self.current_player = self.pool.__next__()

    def addColour_2_player(self, colour_list):
        temp = 0
        for i in self.players:
            i.colour = colour_list[temp]
            temp += 1

    def move(self):
        print("now player {} with colour {} start dice".format(self.current_player.name, self.current_player.colour))
        self.current_player.dice()
        print("player {} got number {}".format(self.current_player.name, self.current_player.number))
        self.current_player.current_position += self.current_player.number
        if not self.isGameEnd():
            # judge if the player trigger the snakes or the ladders
            if self.current_player.current_position in self.snakes.keys():
                self.current_player.current_position = self.snakes[self.current_player.current_position]
                print("snakes!!! player {} back to {}".format(self.current_player.name, self.current_player.current_position))
            if self.current_player.current_position in self.ladders.keys():
                print("ladders!!! player {} Going to {}".format(self.current_player.name, self.current_player.current_position))
            print("player {} now in position {}\n".format(self.current_player.name, self.current_player.current_position))
            self.current_player = self.pool.__next__()
            # judge if the next player is robot.
            if self.current_player.name.split("-")[0] == "robot":
                self.move()



    def isGameEnd(self):
        if self.current_player.current_position == 100:
            # game status equals to 1 means game is ended
            self.game_status = 1
            return True
        # we must ensure the position is accurately equal to 100
        if self.current_player.current_position >= 100:
            self.current_player.current_position -= self.current_player.current_position
            print("You roll a dice greater than 100, back to the previous position: {}".format(self.current_player.current_position))
            # game status equals to 0 means game is not ended
            self.game_status = 0
            return False
        # if current player did not meet the game end request, then conitnue the game
        if self.current_player.current_position < 100:
            print("Current player {} did not meet the end, Game contine".format(self.current_player.name))
            # game status equals to 0 means game is not ended
            self.game_status = 0
            return False
