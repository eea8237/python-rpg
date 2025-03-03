"""
Parent class for player and monster

so, a player has stats such as a max hp, attack, defense, magic, magic points, and speed. They also have a level, 
current hp, exp, and gold.
Their sword, shield, and wand have levels of their own. The player also has a catalogue of items they can find to aid them 
in their quest.
They also have temporary versions of their stats that disappear after a battle ends.

The player will encounter various monsters during their quest. Monsters have the same stats as the player. Different 
species have different skills
that use magic instead of attack and can leave various status effects on the player. Monsters also have elements that 
change what their basic attack is.
By default, all elements deal more damage to a nonelemental
"""
from stat import *
import element
from skill import *
from status_effect import *
from item import *

from random import *

MAX_HP = "Max HP"
MAX_MP = "Max MP"
HP = "HP"
MP = "MP"
ATTACK = "Attack"
DEFENSE = "Defense"
MAGIC = "Magic"
SPEED = "Speed"
# the following should have default values of 0
TEMP_ATTACK = "Temp. ATK"
TEMP_DEFENSE = "Temp. DEF"
TEMP_MAGIC = "Temp. MAG"
TEMP_SPEED = "Temp. SPD"

LEVEL = "Level"
GOLD = "Gold"

FIGHT = "Fight"
DEFEND = "Defend"
ITEM = "Items"
SKILL = "Skill"
FLEE = "Flee"
class Entity:
    __slots__ = ["_stats", "_options", "_skills", "_element", "_status", "_choice", "_name"] # options are attack/defend/items/stat check/run. monsters don't use options

    def __init__(self, name=None, element=element.NONE, options=None, skills=None, status=None):
        self._stats = {MAX_HP:10, # monsters should have diff initial stats
                        HP:10,
                        MAX_MP:10,
                        MP:10,
                        ATTACK:5,
                        DEFENSE:5,
                        MAGIC:5,
                        SPEED:5,
                        TEMP_ATTACK:[0, 0], # 0 is the value, 1 is the counter
                        TEMP_DEFENSE:[0, 0],
                        TEMP_MAGIC:[0, 0],
                        TEMP_SPEED:[0, 0],
                        LEVEL:0,
                        GOLD:0} # in case I want to add a steal thing or something
    # the player will also have exp, a level, and gold, along with temp stats
    # monsters will just have level, along with their name and the type of monster they are

        self._element = element
        self._options = options # stuff player can select
        self._skills = skills # skills that can be used apart apart from basic attack
        self._status = [status, 0] # possible status effects
        self._choice = None
        self._name = name

    def __repr__(self):
        if self._skills is not None:
            skills = [skill.get_name() for skill in self._skills] 
        else:
            skills = self._skills
        return "Entity: " + \
        "\n   Name = " + str(self._name) + \
        "\n   Element = " + str(self._element) + \
        "\n   Status = " + str(self._status) + \
        "\n   Options = " + str(self._options) + \
        "\n   Skills = " + str(skills) + \
        "\n   Stats = " + str(self._stats)
    def __str__(self):
        return str(self._element) + " Entity (" + str(self._stats[HP]) + "/" + str(self._stats[MAX_HP]) + ") [" + str(self._stats[MP]) + "/" + str(self._stats[MAX_MP]) + "]"
    
    def __hash__(self):
        return hash(self._element)
        

    def get_stats(self):
        return dict(self._stats)
    def get_element(self):
        return self._element
    def get_status(self):
        return list(self._status) # it's a list of the effect and its duration
    def get_choice(self):
        return self._choice
    
    def get_hp(self):
        return self._stats[HP]
    def get_mp(self):
        return self._stats[MP]
    def get_hp_string(self):
        return str(self._stats[HP]) + "/" + str(self._stats[MAX_HP])
    def get_mp_string(self):
        return str(self._stats[MP]) + "/" + str(self._stats[MAX_MP])
    def get_level(self):
        return self._stats[LEVEL]
    def get_gold(self):
        return self._stats[GOLD]
    
    def set_element(self, element):
        self._element = element
    def set_status(self, status, duration):
        self._status = [status, duration]
    def set_choice(self, choice):
        self._choice = choice

    def reset_status(self):
        self._status = None

    def add_skill(self, skill):
        self._skills.append(skill) # assume skills is a list of skills

    def increase_HP(self, amount):
        self._stats[HP] += amount
        self.hp_cap()
    def decrease_HP(self, amount):
        self._stats[HP] -= amount
        self.hp_cap()
    def heal_full(self):
        """
        Restore HP to full if need be
        """
        if self._stats[HP] < self._stats[MAX_HP]:
            self._stats[HP] = self._stats[MAX_HP]

    def increase_MP(self, amount):
        self._stats[MP] += amount
        self.mp_cap()
    def decrease_MP(self, amount):
        self._stats[MP] -= amount
        self.mp_cap()

    def addGold(self, amount):
        self._stats[GOLD] += amount
    def loseGold(self, amount):
        self._stats[GOLD] -= amount
        if self._stats[GOLD] < 0:
            self._stats[GOLD] = 0
    def spend_gold(self, amount):
        """
        spend an amount of gold
        """
        if self.gold_check(amount):
            self._stats[GOLD] -= amount
            self.gold_cap()
            return True
        else:
            return False
    def gold_check(self, amount):
        """
        Check if gold is greater than some amount
        """
        return self._stats[GOLD] >= amount

    # implementing options...

    def make_choice(self, other=None, skill=None):
        """
        Choose something to do in battle
        """
        if self._choice == FIGHT:
            self.attack(other)
        elif self._choice == DEFEND:
            self.defend()
        elif self._choice == ITEM:
            self.use_item()
        elif self._choice == SKILL:
            self.use_skill(skill)
        #elif self._choice == FLEE: # - implement in battle? or here? you'd exit the current battle essentially, losing gold if you have any 
            #self.flee() # players and monsters should have different ways to choose - player does it manually, monsters choose randomly (probably weighted)
    
    def attack(self, other):
        """
        Get rid of other's hp
        deals damage based on element, attack, and defense
        crits are also a thing
        """
        '''
        if randint(1, 100) > 100 - sword or (luckyCharm == 1 and randint(1, 100) > 100 - (sword * 2)) :
        damage += 5
        print("Oh! A critical hit!")
        monsterHP -= damage
        if level <= 100:
            print("You dealt", damage, "damage to the monster!")
        else:
            print("You dealt", damage, "damage to the Dragon King!")
        '''
        self_attack = self._stats[ATTACK] + self._stats[TEMP_ATTACK][0]
        other_defense = other._stats[DEFENSE] + other._stats[TEMP_DEFENSE][0]
        crit = 0
        if randint(1, 100) <= 5:
            crit = self_attack

        if self._element.effective(other._element):
            damage = self_attack * 3 + randint(0, 5) - other_defense + crit
        elif self._element.resisted(other._element):
            damage = self_attack + randint(0, 5) - other_defense + crit
        else:
            damage = self_attack * 2 + randint(0, 5) - other_defense + crit
        
        # damage can only be positive
        if damage <= 0:
            damage = 1

        other._stats[HP] -= damage # should damage be calculated here? i guess
        other.hp_cap() # do something with this? or is conscious
        return damage
    
    def defend(self):
        """
        Temporarily double defense
        critical defend? should that only be for the player?
        maybe it adds 999 to the temp defense
        """
        self._stats[TEMP_DEFENSE][0] = self._stats[DEFENSE]
        self._stats[TEMP_DEFENSE][1] = 1 # lasts for 1 turn
        


    def use_skill(self, other, skill):
        """
        Uses a skill on the other
        deals damage based on magic
        """
    # player should also have use_item and flee and check stats, along with overworld options
    # monsters may have a different flee

    def use_item(self, item, other=None):
        if (item.targets_opponent() and other is not None):
            item.use(other)
        else:
            item.use(self)
        

    def speed_check(self, other):
        """
        Returns the entity with the faster speed.
        """
        self_speed = self._stats[SPEED] + self._stats[TEMP_SPEED][0]
        other_speed = other._stats[SPEED] + other._stats[TEMP_SPEED][0]
        if self_speed > other_speed:
            return self
        elif self_speed < other_speed:
            return other
        else:
            # randomly decide
            if randint(0, 1) == 0:
                return self
            else:
                return other
            
    def process_effect(self):
        """
        processes a status effect at the end of a turn
        
        # negative
    WEAKEN = ["Weaken", 0] 
    DECAY = ["Decay", 0] # lower defense
    SLOW = ["Slow", 0] # lower speed
    DISQUIET = ["Disquiet", 0] # lower magic
    POISON = ["Poison", 0] # lose hp
    DRAIN = ["Drain", 0] # lose mp
    FREEZE = ["Freeze", 0] # lose a turn

    # Positive
    STRENGTHEN = ["Strengthen", 0] # boost attack
    FORTIFY = ["Fortify", 0] # boost defense
    HASTEN = ["Hasten", 0] # boost speed
    EMPOWER = ["Empower", 0] # boost magic
    REGENERATE = ["Regenerate", 0] # heal hp
    FOCUS = ["Focus", 0] # heal mp
    SLIPPERY = ["Slippery", 0] # two consecutive turns
        """
        # negative
        if self._status[0] == StatusEffect.WEAKEN:
            # lower attack
            self._stats[TEMP_ATTACK][0] = -self._stats[ATTACK] * 1/2
            self._stats[TEMP_ATTACK][1] = self._status[1]

        elif self._status[0] == StatusEffect.DECAY:
            # lower defense
            self._stats[TEMP_DEFENSE][0] = -self._stats[DEFENSE] * 1/2
            self._stats[TEMP_DEFENSE][1] = self._status[1]

        elif self._status[0] == StatusEffect.DISQUIET:
            # lower magic
            self._stats[TEMP_MAGIC][0] = -self._stats[MAGIC] * 1/2
            self._stats[TEMP_MAGIC][1] = self._status[1]

        elif self._status[0] == StatusEffect.SLOW:
            # lower speed
            self._stats[TEMP_SPEED][0] = -self._stats[SPEED] * 1/2
            self._stats[TEMP_SPEED][1] = self._status[1]

        elif self._status[0] == StatusEffect.POISON:
            # lose HP (at end of turn)
            self.decrease_HP(self._stats[MAX_HP] // 10)

        elif self._status[0] == StatusEffect.DRAIN:
            # lose MP (at end of turn)
            self.decrease_MP(self._stats[MAX_MP] // 10)
        # process freeze during turn handling

        # positive 
        elif self._status[0] == StatusEffect.STRENGTHEN:
            # lower attack
            self._stats[TEMP_ATTACK][0] = self._stats[ATTACK] * 1/2
            self._stats[TEMP_ATTACK][1] = self._status[1]

        elif self._status[0] == StatusEffect.FORTIFY:
            # raise defense
            self._stats[TEMP_DEFENSE][0] = self._stats[DEFENSE] * 1/2
            self._stats[TEMP_DEFENSE][1] = self._status[1]

        elif self._status[0] == StatusEffect.EMPOWER:
            # raise magic
            self._stats[TEMP_MAGIC][0] = self._stats[MAGIC] * 1/2
            self._stats[TEMP_MAGIC][1] = self._status[1]

        elif self._status[0] == StatusEffect.HASTEN:
            # raise speed
            self._stats[TEMP_SPEED][0] = self._stats[SPEED] * 1/2
            self._stats[TEMP_SPEED][1] = self._status[1]

        elif self._status[0] == StatusEffect.REGENERATE:
            # restore HP (at end of turn)
            self.increase_HP(self._stats[MAX_HP] // 10)

        elif self._status[0] == StatusEffect.FOCUS:
            # restore MP (at end of turn)
            self.increase_MP(self._stats[MAX_MP] // 10)


    def is_conscious(self):
        """
        Returns true if HP is above 0 and False if below/at 0.
        """
        return self._stats[HP] > 0


    def hp_cap(self):
        """
        if hp is above max HP, make it equal max HP
        if hp is below 0, make it 0
        """
        if self._stats[HP] > self._stats[MAX_HP]:
            self._stats[HP] = self._stats[MAX_HP]
        elif self._stats[HP] < 0:
            self._stats[HP] = 0

    def mp_cap(self):
        """
        if mp is above max MP, make it equal max MP
        if mp is below 0, make it 0
        """
        if self._stats[MP] > self._stats[MAX_MP]:
            self._stats[MP] = self._stats[MAX_MP]
        elif self._stats[MP] < 0:
            self._stats[MP] = 0

    def gold_cap(self, amount=-1):
        """
        if gold is above a certain amount, make it that amount. - for a gold cap or something
        if gold is below 0, make it 0
        """
        if self._stats[GOLD] > amount and amount != -1:
                self._stats[GOLD] = amount
        elif self._stats[GOLD] < 0:
            self._stats[GOLD] = 0
    