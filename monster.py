"""
Class for Monster
"""
from entity import *
from stat import *
from item import *
import element;

MONSTERS = ["Slime"]

class Monster(Entity):
    # how do slots work with inheritance
    __slots__ = ["__name", "__strength"]

    def __init__(self, name, strength, element=element.NONE):
        super(element, ["Fight", "Defend", "Skills", "Flee"])
        self.__name == name
        self.__strength == strength

    def set_stats(self):
        '''
        
        '''
        