from enum import *
import entity
import element
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
ARMOR = "Armor"
WEAPON = "Weapon"
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

    def enable(self):
        """
        Enables an inactive effect
        """
        # is there a way to check if there's a boolean in effect
        if self._effect == False:
            self._effect = True

    def disable(self):
        """
        Disables an active effect
        """
        # is there a way to check if there's a boolean in effect
        if self._effect == True:
            self._effect = False
    
class KeyItem(Item):
    def __init__(self, name, effect, description):
        super().__init__(name, 0, SPECIAL, True, effect, description)

class Key(Item):
    def __init__(self, name, effect, description):
        super().__init__(name, 0, KEY, True, effect, description)

class Charm(Item):
    GOLD = "Gold+"
    EXP = "EXP+"
    CRIT = "Lucky"
    def __init__(self, name, effect, description):
        super().__init__(name, 0, CHARM, True, effect, description)

class Armor(Item):
    __slots__ = ["_name", "_price", "_type", "_is_key_item", "_effect", "_description", "_on_sale", "_target_opponent", "_element", "_level", "_power"]
    POWER_I = 1
    POWER_II = 3
    POWER_III = 5
    POWER_IV = 7

    POWER_I_NAME = "Normal"
    POWER_II_NAME = "Durable"
    POWER_III_NAME = "Fortified"
    POWER_IV_NAME = "Unbreakable"
    ARMOR_NAME = "Chainmail"
    def __init__(self, name, effect, description, element, power):
        super().__init__(name, 0, ARMOR, True, effect, description)
        self._element = element
        self._level = 0
        self._power = power # the amount of defense this provides
    # keep in mind only one armor will be active at a time
    # Armor may also boost defense somewhat

    def level_up(self):
        self._level += 1
        # have cap?

    def level_down(self):
        self._level -= 1
        self._level = 0 if self._level < 0 else self._level

class Weapon(Armor):
    __slots__ = ["_name", "_price", "_type", "_is_key_item", "_effect", "_description", "_on_sale", "_target_opponent", "_element", "_stat", "_level"]
    POWER_I_NAME = "Regular"
    POWER_II_NAME = "Sleek"
    POWER_III_NAME = "Sharpened"
    POWER_IV_NAME = "Impeccable"
    SWORD_NAME = "Blade"
    WAND_NAME = "Staff"

    def __init__(self, name, effect, description, element, power, stat):
        super().__init__(name, 0, WEAPON, True, effect, description, power)
        self._element = element
        self._stat = stat # the stat the weapon boosts
        self._level = 0
    # keep in mind only one weapon will be active at a time

    def level_up(self):
        self._level += 1
        # have cap?

    def level_down(self):
        self._level -= 1
        self._level = 0 if self._level < 0 else self._level
    
    

class Scroll(Item):
    POTION = "Potion"
    HP_HEAL = "Health"
    MP_HEAL = "Magic"
    def __init__(self, name, price, effect, description):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        super().__init__(name, price, HEAL, False, effect, description)

class StatChange(Item):
    # should effect add status effect to the player/oppenent?
    # maybe have it vary how many turns it lasts
    ENHANCER = "Boost"
    DEHANCER = "Drop"
    PRICE = 50
    def __init__(self, stat, type, price, description):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        name = stat + " " 
        name += StatChange.ENHANCER if type == POWER_UP else StatChange.DEHANCER
        target = False if type == POWER_UP else True
        super().__init__(name, price, type, False, stat, description, target)

class Potion(Item):
    POTION_NAME = "Potion"
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
    def __init__(self, rank, price, effect):
        # for potions, effect should be the stat it heals (HP or MP, and the amount)
        # maybe a tuple (<stat>, <amount>)
        if effect[0] == entity.MP:
            name = Potion.MP_HEAL
        elif effect[0] == entity.HP:
            name = Potion.HP_HEAL
        name += " " + Potion.POTION_NAME + " " + rank
        description = name + " - heals " + str(effect[1])
        description += "MP" if effect[0] == entity.MP else "HP"
        super().__init__(name, price, HEAL, False, effect, description)

    def use(self, creature):
        if self._effect[0] == entity.MP:
            creature.increase_MP(self.effect[1])
        elif self._effect[0] == entity.HP:
            creature.increase_MP(self.effect[1])

class ArmorList(Enum):
    # armor
    NORMAL_ARMOR_I = Armor(Armor.POWER_I_NAME + " " + Armor.ARMOR_NAME, True, "A normal set of chainmail. " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    NORMAL_ARMOR_II = Armor(Armor.POWER_II_NAME + " " + Armor.ARMOR_NAME, True, "A durable set of typical chainmail. " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    NORMAL_ARMOR_III = Armor(Armor.POWER_III_NAME + " " + Armor.ARMOR_NAME, True, "A prime set of typical chainmail. " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    NORMAL_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " " + Armor.ARMOR_NAME, True, "The best set of typical chainmail you can find. " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    WATER_ARMOR_I = Armor(Armor.POWER_I_NAME + " Ocean " + Armor.ARMOR_NAME, True, "A normal set of ocean chainmail. It's marked with the image of rushing waves. " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    WATER_ARMOR_II = Armor(Armor.POWER_II_NAME + " Ocean " + Armor.ARMOR_NAME, True, "A durable set of ocean chainmail. " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    WATER_ARMOR_III = Armor(Armor.POWER_III_NAME + " Ocean " + Armor.ARMOR_NAME, True, "A prime set of ocean chainmail. " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    WATER_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Ocean " + Armor.ARMOR_NAME, True, "The best set of ocean chainmail you can find. " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    FIRE_ARMOR_I = Armor(Armor.POWER_I_NAME + " Flame " + Armor.ARMOR_NAME, True, "A normal set of flame chainmail. Flamemail. " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    FIRE_ARMOR_II = Armor(Armor.POWER_II_NAME + " Flame " + Armor.ARMOR_NAME, True, "A durable set of flamemail. " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    FIRE_ARMOR_III = Armor(Armor.POWER_III_NAME + " Flame " + Armor.ARMOR_NAME, True, "A prime set of flamemail. " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    FIRE_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Flame " + Armor.ARMOR_NAME, True, "The best set of flamemail you can find. " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    PLANT_ARMOR_I = Armor(Armor.POWER_I_NAME + " Forest " + Armor.ARMOR_NAME, True, "A normal set of forest chainmail - " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    PLANT_ARMOR_II = Armor(Armor.POWER_II_NAME + " Forest " + Armor.ARMOR_NAME, True, "A durable set of forest chainmail - " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    PLANT_ARMOR_III = Armor(Armor.POWER_III_NAME + " Forest " + Armor.ARMOR_NAME, True, "A prime set of forest chainmail - " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    PLANT_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Forest " + Armor.ARMOR_NAME, True, "The best set of forest chainmail you can find - " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    EARTH_ARMOR_I = Armor(Armor.POWER_I_NAME + " Earthen " + Armor.ARMOR_NAME, True, "A normal set of earthen chainmail - " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    EARTH_ARMOR_II = Armor(Armor.POWER_II_NAME + " Earthen " + Armor.ARMOR_NAME, True, "A durable set of earthen chainmail - " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    EARTH_ARMOR_III = Armor(Armor.POWER_III_NAME + " Earthen " + Armor.ARMOR_NAME, True, "A prime set of earthen chainmail - " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    EARTH_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Earthen " + Armor.ARMOR_NAME, True, "The best set of earthen chainmail you can find - " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    AIR_ARMOR_I = Armor(Armor.POWER_I_NAME + " Wind " + Armor.ARMOR_NAME, True, "A normal set of wind chainmail - " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    AIR_ARMOR_II = Armor(Armor.POWER_II_NAME + " Wind " + Armor.ARMOR_NAME, True, "A durable set of wind chainmail - " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    AIR_ARMOR_III = Armor(Armor.POWER_III_NAME + " Wind " + Armor.ARMOR_NAME, True, "A prime set of wind chainmail - " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    AIR_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Wind " + Armor.ARMOR_NAME, True, "The best set of wind chainmail you can find - " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    LIGHTNING_ARMOR_I = Armor(Armor.POWER_I_NAME + " Spark " + Armor.ARMOR_NAME, True, "A normal set of electric chainmail - " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    LIGHTNING_ARMOR_II = Armor(Armor.POWER_II_NAME + " Spark " + Armor.ARMOR_NAME, True, "A durable set of electric chainmail - " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    LIGHTNING_ARMOR_III = Armor(Armor.POWER_III_NAME + " Spark " + Armor.ARMOR_NAME, True, "A prime set of electric chainmail - " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    LIGHTNING_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Spark " + Armor.ARMOR_NAME, True, "The best set of electric chainmail you can find - " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    LIGHT_ARMOR_I = Armor(Armor.POWER_I_NAME + " Blinding " + Armor.ARMOR_NAME, True, "A normal set of blinding chainmail - " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    LIGHT_ARMOR_II = Armor(Armor.POWER_II_NAME + " Blinding " + Armor.ARMOR_NAME, True, "A durable set of blinding chainmail - " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    LIGHT_ARMOR_III = Armor(Armor.POWER_III_NAME + " Blinding " + Armor.ARMOR_NAME, True, "A prime set of blinding chainmail - " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    LIGHT_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Blinding " + Armor.ARMOR_NAME, True, "The best set of blinding chainmail you can find - " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)
    
    DARK_ARMOR_I = Armor(Armor.POWER_I_NAME + " Void " + Armor.ARMOR_NAME, True, "A normal set of void chainmail - " + str(Armor.POWER_I) + " GUARD.", element.NONE, Armor.POWER_I)
    DARK_ARMOR_II = Armor(Armor.POWER_II_NAME + " Void " + Armor.ARMOR_NAME, True, "A durable set of void chainmail - " + str(Armor.POWER_II) + " GUARD.", element.NONE, Armor.POWER_II)
    DARK_ARMOR_III = Armor(Armor.POWER_III_NAME + " Void " + Armor.ARMOR_NAME, True, "A prime set of void chainmail - " + str(Armor.POWER_III) + " GUARD.", element.NONE, Armor.POWER_III)
    DARK_ARMOR_IV = Armor(Armor.POWER_IV_NAME + " Void " + Armor.ARMOR_NAME, True, "The best set of void chainmail you can find - " + str(Armor.POWER_IV) + " GUARD.", element.NONE, Armor.POWER_IV)

class ItemList(Enum):
    # key items
    BUBBLE = KeyItem("Bubble", True, "A bubble that prevents damage from the first attack.") # effect should be used to determine if bubble should be active - may need to add way to change effect ?
    GOLD_CHARM = Charm("Gold Charm", True, "A charm that increases the gold earned from battles.")
    LUCKY_CHARM = Charm("Lucky Charm", True, "A charm that increases the chance of a critical hit")
    EXP_CHARM = Charm("EXP Charm", True, "A charm that increases the experience earned from battles.")
    REVIVAL_CHARM = Charm("Revival Charm", True, "A charm that revives you to 25% of your Max HP if you fall in battle once.")
    SILENT_BOOTS = KeyItem("Silent Boots", True, "Boots that increase the chance of successfully fleeing a battle.")
    SILENT_BOOTS_PLUS = KeyItem("Really Silent Boots", True, "Boots that let you flee almost any battle.")
    
    # stat change
    ATK_BOOST = StatChange(entity.ATTACK, POWER_UP, StatChange.PRICE, "Boosts Attack by 1.5x temporarily.")
    DEF_BOOST = StatChange(entity.DEFENSE, POWER_UP, StatChange.PRICE, "Boosts Defense by 1.5x temporarily.")
    MAG_BOOST = StatChange(entity.MAGIC, POWER_UP, StatChange.PRICE, "Boosts Magic by 1.5x temporarily.")
    SPD_BOOST = StatChange(entity.SPEED, POWER_UP, StatChange.PRICE, "Boosts Speed by 1.5x temporarily.")

    ATK_DROP = StatChange(entity.ATTACK, POWER_DOWN, StatChange.PRICE, "Halves opponent's Attack temporarily.")
    DEF_DROP = StatChange(entity.DEFENSE, POWER_DOWN, StatChange.PRICE, "Halves opponent's Defense temporarily.")
    MAG_DROP = StatChange(entity.MAGIC, POWER_DOWN, StatChange.PRICE, "Halves opponent's Magic temporarily.")
    SPD_DROP = StatChange(entity.SPEED, POWER_DOWN, StatChange.PRICE, "Halves opponent's Speed temporarily.")
    '''
    weapons that change the element of the player's default attack
    keys that allow the player to fight the area's boss
        These only have a chance of dropping once the player's fought a certain amount of monsters in an area
        drop chance increases the more monsters the player fights after that
        Once the player has a boss key, they can't get any more
    '''
    # keys
    KEY = Key("Boss Key", True, "A key that shows the way to a boss.")
    
    # potions
    HP_POTION_I = Potion(RANK_I, (entity.HP, Potion.RANK_I_AMOUNT))
    HP_POTION_II = Potion(RANK_II, (entity.HP, Potion.RANK_II_AMOUNT))
    HP_POTION_III = Potion(RANK_III, (entity.HP, Potion.RANK_III_AMOUNT))
    HP_POTION_IV = Potion(RANK_IV, (entity.HP, Potion.RANK_IV_AMOUNT))

    MP_POTION_I = Potion(RANK_I, (entity.MP, Potion.RANK_I_AMOUNT))
    MP_POTION_II = Potion(RANK_II, (entity.MP, Potion.RANK_II_AMOUNT))
    MP_POTION_III = Potion(RANK_III, (entity.MP, Potion.RANK_III_AMOUNT))
    MP_POTION_IV = Potion(RANK_IV, (entity.MP, Potion.RANK_IV_AMOUNT))

    # put in an equals method - maybe in item itself
    # two items are equal if they have the same name
    # items can be sorted by cost
    
    
    