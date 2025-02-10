"""
Status effects include Weaken (lowers attack), Decay (lowers defense), Slow (lowers speed), Disquiet (lowers magic), 
Poison (lowers HP per turn) and Freeze (skips a turn)
Positive status effects do the opposite of this.
Status effects heal after a certain amount of turns.
"""
from enum import Enum
from random import *

class StatusEffect(Enum):
    # actual effects should be handled in entity class
    # negative
    WEAKEN = "Weaken" # lower attack
    DECAY = "Decay" # lower defense
    SLOW = "Slow" # lower speed
    DISQUIET = "Disquiet" # lower magic
    POISON = "Poison" # lose hp
    DRAIN = "Sap" # lose mp
    FREEZE = "Freeze" # lose a turn

    # Positive
    STRENGTHEN = "Strengthen" # boost attack
    FORTIFY = "Fortify" # boost defense
    HASTEN = "Hasten" # boost speed
    EMPOWER = "Empower" # boost magic
    REGENERATE = "Regenerate" # heal hp
    FOCUS = "Focus" # heal mp
    SLIPPERY = "Slippery" # two consecutive turns

    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value

    def __hash__(self):
        return hash(self)
    '''
    def __eq__(self, other):
        if type(self) == type(other):
            return self == other
        else:
            return False'''

'''    def get_duration(self):
        return self[1]

    def set_duration(self, duration):
        self[1] = duration

    def increment_duration(self):
        self[1] += 1

    def decrement_duration(self):
        self[1] -= 1
        if self[1] < 0:
            self[1] = 0'''