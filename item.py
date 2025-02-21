from enum import *
import entity
"""
Parent class for other items

Items include potions and temporary boosts to stats.
Permanent items include:
    bubble that prevents effects until the first damaging attack
    gold charm that increases the gold earned from battles
    lucky charm that increases the chance of a critical hit
    exp charm that boosts exp earned from battles
    silent boots that make the player always able to flee from a battle (or doubles chance of fleeing)
    charms that permanently boost stats
    charms that give the player certain skills
    charms that make the player resist certain types
    armors that make the player certain elements
    weapons that change the element of the player's default attack
    charm that revives the player once when their HP is reduced to 0 
    keys that allow the player to fight the area's boss
        These only have a chance of dropping once the player's fought a certain amount of monsters in an area
        drop chance increases the more monsters the player fights after that
        Once the player has a boss key, they can't get any more

each item has a cost, with a sell value of half that cost. Key items have sell values of 0
Each item is categorized by its effect - healing, power up, power down, armor, scroll, key (literally), and special
    Armor (and weapons), key, maybe scroll, charms and special are all key items
"""

# Categories (maybe make enum)
HEAL = "Recovery"
POWER_UP = "Enhancer"
POWER_DOWN = "Dehancer"
ARMOR = "Armor/Weapon"
SCROLL = "Scroll"
KEY = "Key"
CHARM = "Charm"
SPECIAL = "Special"

# ranks
RANK_I = "I"
RANK_II = "II"
RANK_III = "III"
RANK_IV = "A"
class Item:
    __slots__ = ["_name", "_price", "_type", "_is_key_item", "_effect", "_description", "_on_sale", "_target_opponent"]

    def __init__(self, name, price, type, key_item=False, effect=None, description="", target_opponent=False):
        self._name = name
        self._price = price
        self._type = type
        self._is_key_item = key_item
        self._effect = effect
        self._description = description
        self._on_sale = False
        self._target_opponent = target_opponent;

    def __repr__(self):
        return "Item: " + \
            "\n   Name=" + self._name + \
            "\n   Price=" + str(self._price) + \
            "\n   Type=" + str(self._type) + \
            "\n   Key Item?=" + str(self._is_key_item) + \
            "\n   Additional Effect=" + str(self._effect) + \
            "\n   Description=" + str(self._description) + \
            "\n   Targets Opponent?=" + str(self._target_opponent)
    def __str__(self):
        return self._name + " " + str(self._price) + "gold"
    
    def use(self, entity):
        pass

    def get_name(self):
        return self._name
    def get_price(self):
        if self._on_sale == True:
            return self._price // 2
        else:
            return self._price
    def get_type(self):
        return self._type
    def get_is_key_item(self):
        return self._is_key_item
    def get_effect(self):
        return self._effect
    def get_description(self):
        return self._description
    def get_sell_value(self):
        if self._on_sale == True:
            return self._price // 4
        else:
            return self._price // 2
    def targets_opponent(self):
        return self._target_opponent
    
    def set_on_sale(self, value):
        """
        If an item was bought on sale, treat it as though its price and sell/value are half what they actually are
        """
        self._on_sale = value
    
class KeyItem(Item):
    def __init__(name, effect, description):
        super().__init__(name, 0, SPECIAL, True, effect, description)

class Key(Item):
    def __init__(name, effect, description):
        super().__init__(name, 0, KEY, True, effect, description)

class Charm(Item):
    def __init__(name, effect, description):
        super().__init__(name, 0, CHARM, True, effect, description)

class Armor(Item):
    def __init__(name, effect, description):
        super().__init__(name, 0, ARMOR, True, effect, description)

class Scroll(Item):
    POTION = "Potion"
    HP_HEAL = "Health"
    MP_HEAL = "Magic"
    def __init__(name, price, effect, description):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        super().__init__(name, price, HEAL, False, effect, description)

class StatChange(Item):
    ENHANCER = "Boost"
    DEHANCER = "Drop"
    ENHANCE = True # or false if it lowers stat
    def __init__(stat, type, price, effect, description, target):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        name = stat + " " 
        name += StatChange.ENHANCER if type == POWER_UP else StatChange.DEHANCER
        super().__init__(name, price, type, False, effect, description)

class Potion(Item):
    POTION = "Potion"
    HP_HEAL = "Health"
    MP_HEAL = "Magic"

    RANK_I_AMOUNT = 20
    RANK_II_AMOUNT = 50
    RANK_III_AMOUNT = 100
    RANK_IV_AMOUNT = 9999
    HP_I_COST = 10
    HP_II_COST = 25
    HP_III_COST = 50
    HP_IV_COST = 100
    MP_I_COST = 12
    MP_II_COST = 30
    MP_III_COST = 60
    MP_IV_COST = 120
    def __init__(name, price, effect, description):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        # maybe a tuple (<stat>, <amount>)
        super().__init__(name, price, HEAL, False, effect, description)

    def use(self, creature):
        if self._effect[0] == entity.MP:
            creature.increase_MP(self.effect[1])
        elif self._effect[1] == entity.HP:
            creature.increase_MP(self.effect[1])

class ItemList(Enum):
    HP_POTION_I = Potion()
    
    
    