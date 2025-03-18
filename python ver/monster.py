"""
Class for Monster
"""
from entity import *
from stat import *
from item import *
from enum import *
import element
import random


class Monster(Entity):
    # how do slots work with inheritance
    __slots__ = ["__name", "__strength", "__items", "__skills", "__level_range"]
    #strengths
    WEAK = 0
    NORMAL = 1
    STRONG = 2
    GOLD = 4
    BOSS = 5

    def __init__(self, name, strength, levelRange=None, element=element.NONE, skills=None):
        super(element, ["Fight", "Defend", "Skills", "Flee"])
        full_name = name
        if strength != Monster.NORMAL:
            prefix = MonsterNames.WEAK if strength == Monster.WEAK else MonsterNames.STRONG if strength == Monster.STRONG else MonsterNames.GOLD if strength == Monster.GOLD else MonsterNames.BOSS
            if strength == Monster.BOSS:
                full_name += " " + prefix #technically suffix 
            else: 
                full_name = prefix + " " + full_name
        if element != element.NONE:
            full_name = str(element) + " " + full_name

        self.__name == full_name
        self.__strength == strength
        self.__skills = skills
        # level range is a tuple with min and max levels for an area
        # can override level with set stats or set level
        self._stats[LEVEL] = random.randint(levelRange[0], levelRange[1]) if levelRange is not None else 1
        self.__update_stats()

    def set_level(self, level): 
        self._stats[LEVEL] = level
        self.__update_stats()

    def set_level_with_range(self, levelRange): 
        level = random.randint(levelRange[0], levelRange[1])
        self._stats[LEVEL] = level # update stats with level increase
        self.__update_stats()

    def __update_stats(self):
        """
        Update stats for appropriate level
        """
        self.__init_stats()
        self._stats[ATTACK] *= self._stats[LEVEL]
        self._stats[DEFENSE] *= self._stats[LEVEL]
        self._stats[MAGIC] *= self._stats[LEVEL]
        self._stats[SPEED] *= self._stats[LEVEL]
        self._stats[GOLD] *= self._stats[LEVEL]
        self._stats[MAX_HP] *= self._stats[LEVEL] // 2
        self._stats[HP] *= self._stats[MAX_HP]
        self._stats[MAX_MP] *= self._stats[LEVEL] // 2
        self._stats[MP] *= self._stats[MAX_MP]

    def __init_stats(self, attack=None, defense=None, magic=None, speed=None, gold=None, maxHP=None, maxMP=None):
        '''
        Set the stats of a monster on its creation (depending on strength)
        The stats defined her are base stats (by default)
        '''
        # if base stats are none, set them to something depending on strength
        default = 1 if self.__strength == Monster.WEAK else 2 if self.__strength == Monster.NORMAL else 3 if self.__strength == Monster.STRONG else 4 if self.__strength == Monster.GOLD else 6
        defaultGold = self._stats[LEVEL]
        attack = default if attack is None else attack
        defense = default if defense is None else defense
        magic = default if magic is None else magic
        speed = default if speed is None else speed
        gold = defaultGold if gold is None else gold
        maxHP = default * 5 if maxHP is None else maxHP
        maxMP = default * 5 if maxMP is None else maxMP
        
        bound = 2 if self.__strength == Monster.WEAK else 7 if self.__strength == Monster.GOLD else 5
        deviation = random.randint(-bound, bound)
        self._stats[ATTACK] = attack + deviation
        self._stats[DEFENSE] = defense + deviation
        self._stats[MAGIC] = magic + deviation
        self._stats[SPEED] = speed + deviation
        self._stats[GOLD] = gold + deviation
        self._stats[MAX_HP] = maxHP + deviation
        self._stats[HP] = self._stats[MAX_HP]
        self._stats[MAX_MP] = maxMP + deviation
        self._stats[MP] = self._stats[MAX_MP]

        for stat in self._stats:
            if self._stats[stat] <= 0:
                self._stats[stat] = 1
        
    # note that when defeated, monsters give gold (and maybe items, along with exp)
    # create a method for on defeat?
    def on_defeat(self, player):
        """
        Give gold and exp
        """
        gold = self._stats[GOLD]
        gold *= 2 if player.item_check(ItemList.GOLD_CHARM) else 1
        player.addGold(gold)
        exp = self._stats[LEVEL] * random.randint(3, 5)
        exp *= 2 if player.item_check(ItemList.EXP_CHARM) else 1
        player.add_exp(exp)
        


class MonsterNames(Enum):
    #modifiers (excluding elements)
    GOLD = "Gold"
    WEAK = "Lesser"
    STRONG = "Greater"
    BOSS = "Lord"
    #names
    SHAPELESS = "Shapeless"
    COCKATRICE = "Cockatriangle"
    EEL = "Squeel"
    ANGEL = "Rectangel"
    WOLF = "Wolfazoid"
    SIREN = "Diamaid"
    WITCH = "Pentawitch"
    ARMADILLO = "Hexadillo"
    SENTRY = "Septry"
    OCTOPUS = "Octapus"
    EVIL_PLANT = "Arnona" # like aroma
    ZOMBIE = "Decaygon"
    CRAB = "Craboss" # like cross
    SNAKE = "Stake"
    GUARDIAN = "Guaircle"
    RIPPLE = "Roval"
    
    DRAGON_IMP = "Dragimp"
    DRAGON_WIZARD = "Drakozard"
    DRAGON_KNIGHT = "Draknight"
    LOWER_DRAGON = "Dragon"

    THIEF = "Thief"
    EVIL_PRIEST = "Priest"
    CIVILIAN = "Shapian"
    
    

class MonsterList(Enum):
    WEAK_SHAPELESS = Monster(MonsterNames.SHAPELESS, Monster.WEAK)
    NORMAL_SHAPELESS = Monster(MonsterNames.SHAPELESS, Monster.NORMAL)
    STRONG_SHAPELESS = Monster(MonsterNames.SHAPELESS, Monster.WEAK)
    GOLD_SHAPELESS = Monster(MonsterNames.SHAPELESS, Monster.WEAK)
    BOSS_SHAPELESS = Monster(MonsterNames.SHAPELESS, Monster.BOSS)