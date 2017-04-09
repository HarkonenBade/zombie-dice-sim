#! /bin/python3

import enum

from termcolor import cprint


class Sides(enum.Enum):
    SHOTGUN = "SHOTGUN"
    FEET = "FOOTSTEPS"
    BRAIN = "BRAIN"


class Die(object):
    def __init__(self):
        self.color = ""
        self.side = ""

    def roll(self):
        raise NotImplementedError()

    def print(self):
        cprint("[{}]".format(self.side.value), self.color)



