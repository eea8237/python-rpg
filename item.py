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

# Categories
HEAL = "Recovery"
POWER_UP = "Enhancer"
POWER_DOWN = "Dehancer"
ARMOR = "Armor/Weapon"
SCROLL = "Scroll"
KEY = "Key"
CHARM = "Charm"
SPECIAL = "Special"

# ranks
NORMAL = "I"
GOOD = "II"
GREAT = "III"
MAX = "A"
class Item:
    __slots__ = ["_name", "_price", "_type", "_is_key_item", "_effect", "_description", "_on_sale"]

    def __init__(self, name, price, type, key_item=False, effect=None, description=""):
        self._name = name
        self._price = price
        self._type = type
        self._is_key_item = key_item
        self._effect = effect
        self._description = description
        self._on_sale = False

    def __repr__(self):
        return "Item: " + \
            "\n   Name=" + self._name + \
            "\n   Price=" + str(self._price) + \
            "\n   Type=" + str(self._type) + \
            "\n   Key Item?=" + str(self._is_key_item) + \
            "\n   Additional Effect=" + str(self._effect) + \
            "\n   Description=" + str(self._description)
    def __str__(self):
        return self._name + " " + str(self._price) + "gold"
    
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
    
    def set_on_sale(self, value):
        """
        If an item was bought on sale, treat it as though its price and sell/value are half what they actually are
        """
        self._on_sale = value
    
class Potion(Item):
    POTION = "Potion"
    HP_HEAL = "Health"
    MP_HEAL = "Magic"
    def __init__(name, price, effect, description):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        super().__init__(name, price, HEAL, False, effect, description)
    
        
    
    
    
    