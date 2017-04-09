#! /bin/python3

import enum
import random


from termcolor import colored, cprint


class Sides(enum.Enum):
    SHOTGUN = "SHOTGUN"
    FEET = "FOOTSTEPS"
    BRAIN = "BRAIN"


class Die(object):
    def __init__(self):
        self.color = ""
        self.side = ""
        self.sides = []

    def roll(self):
        self.side = random.choice(self.sides)
        return self.side

    def disp(self):
        cprint("[{}]".format(self.side.value), self.color)


class RedDie(Die):
    def __init__(self):
        super().__init__()
        self.color = "red"
        self.sides = [Sides.SHOTGUN]*3 + [Sides.FEET]*2 + [Sides.BRAIN]


class YellowDie(Die):
    def __init__(self):
        super().__init__()
        self.color = "yellow"
        self.sides = [Sides.SHOTGUN]*2 + [Sides.FEET]*2 + [Sides.BRAIN]*2


class GreenDie(Die):
    def __init__(self):
        super().__init__()
        self.color = "green"
        self.sides = [Sides.SHOTGUN] + [Sides.FEET]*2 + [Sides.BRAIN]*3


def standard_dice_pot():
    pot = []
    for _ in range(6):
        pot.append(GreenDie())
    for _ in range(4):
        pot.append(YellowDie())
    for _ in range(3):
        pot.append(RedDie())
    return pot


class GameState(object):
    def __init__(self, pot=None, interactive=True):
        if pot is None:
            self.pot = standard_dice_pot()
        else:
            self.pot = pot
        random.shuffle(self.pot)
        self.brains = 0
        self.shotguns = 0
        self.hand = []
        self.interactive = interactive

    def can_continue(self):
        return self.brains + self.shotguns < 13 and self.shotguns < 3

    def score(self):
        return self.brains if self.shotguns < 3 else 0

    def roll(self):
        while len(self.hand) < 3 and len(self.pot):
            self.hand.append(self.pot.pop())
        for d in self.hand:
            s = d.roll()
            if s == Sides.BRAIN:
                self.brains += 1
            elif s == Sides.SHOTGUN:
                self.shotguns += 1
            if self.interactive:
                d.disp()
        if self.interactive:
            print("Brains: {}".format(self.brains))
            print("Shotguns: {}".format(self.shotguns))
            print("Hand: {}".format(" ".join([colored("[D]", d.color)
                                              for d in self.hand])))
        self.hand = [d for d in self.hand if d.side == Sides.FEET]
