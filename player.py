"""
Class for player
"""
from entity import *
from stat import *
import item
import element
import town
import world
import wilds

EXP = "EXP"
class Player(Entity):
    __slots__ = ["_stats", "_options", "_skills", "_element", "_status", "_choice", "_name", "_armor", "_key_items", "_items", "_recent_inn", "_current_world", "_location"] # options are attack/defend/items/stat check/run. monsters don't use options
    
    def __init__(self, name="Bertha"):
        super().__init__(element.NONE, [FIGHT, DEFEND, ITEM, SKILL, FLEE])
        self._stats[EXP] = 0
        self._name = name
        self._armor = None
        self._choice = None
        self._items = {}
        self._key_items = {}
        self._recent_inn = None
        self._current_world = None
        self._location = None # this should start as world 1

    def __str__(self):
        return self._name + " (Level " + str(self._stats[LEVEL]) + ")"
    
    def get_options(self):
        return list(self._options)
    
    def get_items(self, key_item): # key item should be a boolean
        # also, maybe items should be a list of lists or something? where each list contains the item and the amount of the item in the inventory?
        if key_item:
            return dict(self._key_items)
        else:
            return dict(self._items)
    
    def get_exp(self):
        return self._stats[EXP]
    def get_recent_inn(self):
        return str(self._recent_inn)
    def get_current_world(self):
        return str(self._current_world)
    
    def set_recent_inn(self, inn):
        self._recent_inn = inn
    def set_current_world(self, world):
        self._current_world = world
    
    def add_exp(self, amount):
        self._stats[EXP] += amount
    
    def add_item(self, item, key_item=False):
        # will also need to change this if we're making it a dict of lists
        # add the item's name as a key, then the item itself, then the amount of the item
        if key_item:
            if item.get_name() in self._key_items:
                self._key_items[item.get_name()][1] += 1
            else:
                self._key_items[item.get_name()] = [item, 1]
        else:
            if item.get_name() in self._items:
                self._items[item.get_name()][1] += 1
            else:
                self._items[item.get_name()] = [item, 1]

    # could also add a method for checking if item is in items
    # and also a method to see the inventory in general

    def remove_item(self, item, key_item=False):
        # assuming we're doing the amount thing...
        # change this so that it either decrements the amount or removes it from the dict
        # but what if item is bought on sale?
        # maybe include 3rd parameter...? idk
        if key_item:
            if item.get_name() in self._key_items:
                if self._key_items[item.get_name()][1] > 1:
                    self._key_items[item.get_name()][1] -= 1
                else:
                    self._key_items.pop(item)
        else:
            if item.get_name() in self._items:
                if self._items[item.get_name()][1] > 1:
                    self._items[item.get_name()][1] -= 1
                else:
                    self._items.pop(item)
    
    def item_check(self, item, key_item = False):
        if key_item:
            if item.get_name() in self._key_items:
                return True
            else:
                return False
        else:
            if item.get_name() in self._items:
                return True
            else:
                return False
        
    def use_item(self, item, other=None):
        if (item.targets_opponent() and other is not None):
            item.use(other)
        else:
            item.use(self)
        if (item.get_is_key_item()):
            item.disable()
        else:
            self.remove_item(item)

    def level_up_check(self):
        """
        Returns True or False depending on whether or not the player has enough EXP to level up.
        """
        if self._stats[LEVEL] == 0:
            return self._stats[EXP] >= 10
        else:
            return self._stats[EXP] >= self._stats[LEVEL] * 25
        
    def get_to_next_level(self):
        amount = 0
        if self._stats[LEVEL] == 0:
            amount = 10 - self._stats[EXP]
        else:
            amount = self._stats[LEVEL] * 25 - self._stats[EXP]
        if amount < 0:
            amount = 0
        return amount

    def level_up(self):
        """
        Raise stats by 1, HP and MP by 5. Recover HP and MP.
        (maybe 1 * armor level or something)
        """
        if self.level_up_check():
            self._stats[LEVEL] += 1
            self._stats[EXP] = 0
            self._stats[MAX_HP] += 5
            self._stats[HP] = self._stats[MAX_HP] # check if HP is above max hp first?
            self._stats[MAX_MP] += 5
            self._stats[MP] = self._stats[MAX_MP] # check if MP is above max mp first?
            self._stats[ATTACK] += 1
            self._stats[DEFENSE] += 1
            self._stats[MAGIC] += 1
            self._stats[SPEED] += 1
            # maybe there should be a charm that gives gold on level up
        

    