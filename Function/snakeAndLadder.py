import time
from datetime import datetime
from itertools import cycle
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
        self.current_player = None
        self.players = []
        self.snakes = {99: 69, 91: 61, 87: 57, 65: 52, 47: 19, 34: 1, 25: 5}
        self.ladders = {68: 98, 63: 95, 3: 51, 36: 55, 20: 70, 6: 27}
        # self.ladders = {69: 98, 63: 95, 3: 4, 36: 55, 29: 70, 6: 19}
        self.pool = None

    def addPlayer(self, player_list):
        # add player object into player list
        if self.players == []:
            for i in player_list:
                # judge weather it is a robot
                if not i == "":
                    self.players.append(player(i))
                else:
                    random_name = "Player" + "-" + str(datetime.now().microsecond)
                    self.players.append(player(random_name))
            temp = 1
            for i in self.players:
                i.No = temp
                temp += 1
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

    def addAttribute_2_player(self, attribute_list):
        temp = 0
        for i in self.players:
            i.attribute = attribute_list[temp]
            temp += 1

    def move(self):
        self.current_player.current_position += self.current_player.number

    def triggerWhat(self):
        # judge if the player trigger the snakes or the ladders
        if self.current_player.current_position in self.snakes.keys():
            self.current_player.current_position = self.snakes[self.current_player.current_position]
            print("snakes!!! player {} back to {}".format(self.current_player.name,
                                                          self.current_player.current_position))
            return True
        elif self.current_player.current_position in self.ladders.keys():
            self.current_player.current_position = self.ladders[self.current_player.current_position]
            print("ladders!!! player {} Going to {}".format(self.current_player.name,
                                                            self.current_player.current_position))
            return True
        else:
            print("player did not trigger any snake or ladder")
            return False

    def isGameEnd(self):
        end_point = 100
        if self.current_player.current_position == end_point:
            # game status equals to 1 means game is ended
            return True
        # we must ensure the position is accurately equal to 100
        if self.current_player.current_position >= end_point:
            self.current_player.current_position -= self.current_player.number
            print("You roll a dice greater than {}, back to the previous position: {}".format(end_point,
                self.current_player.current_position))
            # game status equals to 0 means game is not ended
            return False
        # if current player did not meet the game end request, then conitnue the game
        if self.current_player.current_position < end_point:
            print("Current player {} did not meet the end, Game continue".format(self.current_player.name))
            # game status equals to 0 means game is not ended
            return False
