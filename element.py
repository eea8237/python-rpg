from enum import *

NAMES_LIST = ["Nonelemental", "Water", "Fire", "Plant", "Earth", "Air", "Lightning", "Light", "Dark", "All"]

class Element():

    __slots__ = ["__name", "__effective", "__resisted"]

    def __init__(self, name=None, effective=None, resist=None):
        self.__name = name
        self.__effective = effective # another element
        self.__resisted = resist # another element(s)

        
    def __lt__(self, other):
        if type(self) == type(other):
            return self.__name < other.__name
        else:
            return False
        
    def __gt__(self, other):
        if type(self) == type(other):
            return self.__name > other.__name
        else:
            return False
        
    def __eq__(self, other):
        # elements are equal if they have the same name
        if type(self) == type(other):
            return self.__name == other.__name
        else:
            return False
        
    def __hash__(self):
        return hash(self.__name)
    
    def __str__(self):
        return self.__name
    
    def __repr__(self):
        resists = self.__resisted
        if str(type(self.__resisted)) == "<class 'set'>":
            resists = set()
            temp = set(self.__resisted)
            while len(temp) > 0:
                resists.add(temp.pop())

        return self.__name + \
               "\n   effective against: " + self.__effective + \
               "\n   resists: " + str(resists)

    
    def effective(self, other):
        """
        returns true if this element is effective against another element
        false otherwise
        """
        # NONE is weak to every element except itself
        return self.__effective == other.__name or (other.__name == NAMES_LIST[0] and self.__name != NAMES_LIST[0])

    def resisted(self, other):
        """
        returns true if this element is resisted by another element
        false otherwise
        """
        if self.__resisted is None:
            return False
        elif self.__resisted == NAMES_LIST[9] and other.__name != NAMES_LIST[0]: # if nonelemental facing not nonelemental (resist is all)
            return True
        elif (other.__name == NAMES_LIST[7]) and (self.__name in {NAMES_LIST[4], NAMES_LIST[5], NAMES_LIST[6]}):
            # if the other is light and self is earth, air, or lightning
            return True
        elif (other.__name == NAMES_LIST[8]) and (self.__name in {NAMES_LIST[1], NAMES_LIST[2], NAMES_LIST[3]}):
            # if the other is dark and self is water, fire, or plant
            return True
        else:
            return other.__name == self.__resisted
        


# make this an enum probably
NONE = Element(NAMES_LIST[0], None, NAMES_LIST[9]) # resisted by all (except none)
WATER = Element(NAMES_LIST[1], NAMES_LIST[2], NAMES_LIST[3]) # effective against fire, resisted by plant
FIRE = Element(NAMES_LIST[2], NAMES_LIST[3], NAMES_LIST[1]) # effective - plant, resisted - water 
PLANT = Element(NAMES_LIST[3], NAMES_LIST[1], NAMES_LIST[2]) # effective - water, resisted - fire
EARTH = Element(NAMES_LIST[4], NAMES_LIST[6], NAMES_LIST[5]) # effective - lightning, resisted - air
AIR = Element(NAMES_LIST[5], NAMES_LIST[4], NAMES_LIST[6]) # effective - earth, resisted - lightning
LIGHTNING = Element(NAMES_LIST[6], NAMES_LIST[5], NAMES_LIST[4]) # effective - air, resisted - earth
LIGHT = Element(NAMES_LIST[7], NAMES_LIST[8], None) # effective - dark
DARK = Element(NAMES_LIST[8], NAMES_LIST[7], None) # effective - light
ALL = Element(NAMES_LIST[9], NONE, None) # effective - NONE

