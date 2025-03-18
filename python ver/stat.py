"""
max hp, attack, defense, magic, magic points, and speed. They also have a level, current hp, exp, and gold.
Their sword, shield, and wand have levels of their own. The player also has a catalogue of items they can find to aid 
them in their quest.
They also have temporary versions of their stats that disappear after a battle ends.
"""

from enum import Enum

class Stat(Enum):
    # can be used alongside a tuple and the actual value or something
    # maybe a dict
    MAX_HP = "Max HP"
    MAX_MP = "Max MP"
    HP = "HP"
    MP = "MP"
    ATTACK = "Attack"
    DEFENSE = "Defense"
    MAGIC = "Magic"
    SPEED = "Speed"
    # the following should have default values of 0
    TEMP_ATTACK = "Temp. Attack"
    TEMP_DEFENSE = "Temp. Defense"
    TEMP_MAGIC = "Temp. Magic"
    TEMP_SPEED = "Temp. Speed"
    
    # the player will also have exp, a level, and gold, along with temp stats
    # monsters will just have level