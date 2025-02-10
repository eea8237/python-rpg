"""
Class for a town

A town has a shop, an inn, and an entrance into the wilds.
"""
import entity
import player
import monster
"""
# Shop handling.
def shop():
    # Shows the current amount of gold.
    print("Gold:", gold)
    
    # Greeting upon entering the store.
    print("The shopkeeper greets you. What do you want to buy?")
    answer = input("Sword upgrade, shield upgrade, armor upgrade, or items? ")
    # Invalid answer handling.
    while answer != "sword" and answer != "shield" and answer != "armor" and answer != "Sword" and answer != "Shield" and answer != "Armor" and answer != "sword upgrade" and answer != "shield upgrade" and answer != "armor upgrade" and answer != "Sword Upgrade" and answer != "Shield Upgrade" and answer != "Armor Upgrade" and answer != "Sword upgrade" and answer != "Shield upgrade" and answer != "Armor upgrade" and answer != "sword Upgrade" and answer != "shield Upgrade" and answer != "armor Upgrade" and answer != "items" and answer != "Items":
        print(answer, "is an invalid answer.")
        answer = input("Sword upgrade, shield upgrade, armor upgrade, or items? ")
    # Alternate Sword Upgrade answers
    if answer == "Sword" or answer == "Sword Upgrade" or answer == "Sword upgrade" or answer == "sword Upgrade":
        answer = "sword"
    # Alternate Shield Upgrade answers
    if answer == "Shield" or answer == "Shield Upgrade" or answer == "Shield upgrade" or answer == "shield Upgrade":
        answer = "shield"
    # Alternate Armor Upgrade answers
    if answer == "Armor" or answer == "Armor Upgrade" or answer == "Armor upgrade" or answer == "armor Upgrade":
        answer = "armor"
    # Alternate Items answers
    if answer == "Items":
        answer = "items"
    # When the player chooses to buy a sword upgrade:
    if answer == "sword":
        if gold < (sword + 1) * 50:
            # Player doesn't have enough money.
            print("You don't have enough gold. This upgrade costs", (sword + 1) * 50, "gold.")
        else:
            # Successful purchase.
            gold -= (sword + 1) * 50
            print("You spent", (sword + 1) * 50, "on the upgrade.")
            sword += 1
            attack += sword
            print("Your sword is now Level", sword, "!")
    # When the player chooses to buy a shield upgrade:
    if answer == "shield":
        if gold < (shield + 1) * 50:
            # Player doesn't have enough money.
            print("You don't have enough gold. This upgrade costs", (shield + 1) * 50, "gold.")
        else:
            # Successful purchase.
            gold -= (shield + 1) * 50
            print("You spent", (shield + 1) * 50, "on the upgrade.")
            shield += 1
            defense += shield
            print("Your shield is now Level", shield, "!")
    # When the player chooses to buy an armor upgrade:
    if answer == "armor":
        if gold < (armor + 1) * 75:
            # Player doesn't have enough money.
            print("You don't have enough gold. This upgrade costs", (armor + 1) * 75, "gold.")
        else:
            # Successful purchase.
            gold -= (armor + 1) * 75
            print("You spent", (armor + 1) * 75, "on the upgrade.")
            armor += 1
            maxhp += armor
            print("Your armor is now Level", armor, "!")
    # When the player chooses to buy items:
    if answer == "items":
        answer = input("Healing Potion - 25, Attack Brew - 25, Defense Brew - 25, Speed Brew - 25, Bubble - 50, EXP Charm - 75, Gold Charm - 150, Lucky Charm - 100, or Silent Boots, 30?: ")
        if answer == "Healing Potion" or answer == "Healing" or answer == "Potion" or answer == "Heal" or answer == "potion" or answer == "healing" or answer == "heal":
            answer = "healing potion"
        # Alternate answer handling
        elif answer == "speed"  or answer == "Speed" or answer == "Speed Brew":
            answer = "speed brew"
        elif answer == "attack"  or answer == "Attack" or answer == "Attack Brew":
            answer = "attack brew"
        elif answer == "defense"  or answer == "Defense" or answer == "Defense Brew":
            answer = "defense brew"
        elif answer == "Bubble":
            answer = "bubble"
        elif answer == "Gold charm" or answer == "Gold" or answer == "Gold Charm" or answer == "gold Charm":
            answer = "gold charm"
        elif answer == "EXP charm" or answer == "EXP" or answer == "EXP Charm" or answer == "Exp Charm":
            answer = "exp charm"
        elif answer == "Luck charm" or answer == "Luck" or answer == "Lucky charm" or answer == "Lucky" or answer == "Lucky Charm" or answer == "Luck Charm" or answer == "luck Charm" or answer == "lucky Charm":
            answer = "lucky charm"
        elif answer == "Silent Boots" or answer == "boots" or answer == "Boots":
            answer = "silent boots"
        # Invalid answer handling.
        while answer != "healing potion" and answer != "attack brew" and answer != "defense brew" and answer != "speed brew" and answer != "exp charm" and answer != "gold charm" and answer != "lucky charm" and answer != "silent boots" and answer != "bubble":
            print(answer, "is an invalid answer.")
            answer = input("Healing Potion - 25, Attack Brew - 25, Defense Brew - 25, Speed Brew - 25, Bubble - 50, EXP Charm - 75, Gold Charm - 150, Lucky Charm - 100, or Silent Boots, 30?: ")
            if answer == "Healing Potion" or answer == "Healing" or answer == "Potion" or answer == "Heal" or answer == "potion" or answer == "healing" or answer == "heal":
                answer = "healing potion"
            elif answer == "speed"  or answer == "Speed" or answer == "Speed Brew":
                answer = "speed brew"
            elif answer == "attack"  or answer == "Attack" or answer == "Attack Brew":
                answer = "attack brew"
            elif answer == "defense"  or answer == "Defense" or answer == "Defense Brew":
                answer = "defense brew"
            elif answer == "Bubble":
                answer = "bubble"
            elif answer == "Gold charm" or answer == "Gold" or answer == "Gold Charm" or answer == "gold Charm":
                answer = "gold charm"
            elif answer == "EXP charm" or answer == "EXP" or answer == "EXP Charm" or answer == "Exp Charm":
                answer = "exp charm"
            elif answer == "Luck charm" or answer == "Luck" or answer == "Lucky charm" or answer == "Lucky" or answer == "Lucky Charm" or answer == "Luck Charm" or answer == "luck Charm" or answer == "lucky Charm":
                answer = "lucky charm"
            elif answer == "Silent Boots" or answer == "boots" or answer == "Boots":
                answer = "silent boots"
        # If the player chooses to buy a Healing Potion.
        if answer == "healing potion":
            if gold < 25:
                print("You don't have enough gold.")
            else:
                gold -= 25
                hp += 25
                hpCheck()
                print("Your HP was restored by 25 points!")
        # If the player chooses to buy an Attack Brew.
        if answer == "attack brew":
            if gold < 25:
                print("You don't have enough gold.")
            else:
                gold -= 25
                attack += level
                print("Your Attack has increased by", level, "!")
        # If the player chooses to buy a Defense Brew.
        if answer == "defense brew":
            if gold < 25:
                print("You don't have enough gold.")
            else:
                gold -= 25
                defense += level
                print("Your Defense has increased by", level, "!")
        # If the player chooses to buy a Speed Brew.
        if answer == "speed brew":
            if gold < 25:
                print("You don't have enough gold.")
            else:
                gold -= 25
                speed += level
                print("Your Speed was increased by", level, "!")
        # If the player chooses to buy a Bubble.
        if answer == "bubble":
            if bubble == 2:
                if gold < 50:
                    print("You don't have enough gold.")
                else:
                    gold -= 50
                    bubble = 1
                    print("A protective bubble will now block the first hit of every battle!")
            else:
                print("You already purchased this.")
        
        # Special Items
        
        # If the player chooses to buy a Gold Charm.
        if answer == "gold charm":
            if goldCharm == 0:
                if gold == 150:
                    print("You don't have enough gold.")
                else:
                    gold -= 150
                    goldCharm = 1
                    print("You can now earn more gold from battles!")
            else:
                print("You already purchased this.")
        # If the player chooses to buy an EXP Charm.
        if answer == "exp charm":
            if expCharm == 0:
                if gold < 75:
                    print("You don't have enough gold.")
                else:
                    gold -= 75
                    expCharm = 1
                    print("You can now earn more EXP from battles!")
            else:
                print("You already purchased this.")
        # If the player chooses to buy a Lucky Charm.
        if answer == "lucky charm":
            if luckyCharm == 0:
                if gold < 100:
                    print("You don't have enough gold.")
                else:
                    gold -= 100
                    luckyCharm = 1
                    print("You now have a higher chance of getting a critical!")
            else:
                print("You already purchased this.")
        # If the player chooses to buy Silent Boots.
        if answer == "silent boots":
            if silentBoots == 0:
                if gold < 30:
                    print("You don't have enough gold.")
                else:
                    gold -= 30
                    silentBoots = 1
                    print("You now have a higher chance to escape from battle!")
            else:
                print("You already purchased this.")
"""
class Shop():
    __slots__ = ["__name", "__items", "__sale"]

    def __init__(self, name="Shop", items={}):
        self.__name = name
        self.__items = items # item is a dict containing the item name, then the item itself + stock? stock can reset when the world changes, or when the player gets a game over
        self.__sale = False

    def get_items(self):
        return dict(self.__items)
    
    def purchase_item(self, player, item):
        if item in self.__items: # check if item (string) is in shop
            if player.get_gold() >= self.__items[item][0].get_cost(): # check if player has enough dough
                if self.__items[item][1] > 0: # check stock
                    # add item to player items
                    player.add_item(item) # show purchased item
                    player.lose_gold(item) # maybe print gold afterwards
                    return True # because it's a success
                else:
                    # presumably check this tuple to see why it failed
                    # in this case, the item is out of stock
                    return False, 2
            else:
                # player doesn't have enough money
                return False, 1
        else:
            # item isn't at shop
            return False, 0
        
    # method for selling items
    # keep in mind you can't sell an item with a sell value of 0



class Inn():
    __slots__ = ["__name", "__cost"]
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def __str__(self):
        return self.__name
    def get_cost(self):
        return self.__cost
    
    # method for recovering player
    """
    def inn():
    global gold
    global hp
    global maxhp
    global answer
    if hp == 0:
        # For when the inn is called by gameover()
        hp = maxhp
        print("You awaken in the inn with your HP restored!")
    else:
        print("The inn charges", level * 5, "gold for a full night's rest.")
        answer = input("Stay at inn, leave: ")
        if answer == "Stay":
            answer = "stay"
        if answer == "Leave":
            answer = "leave"
        while answer != "stay" and answer != "leave":
            print(answer, "is an invalid answer.")
            answer = input("Stay at inn, leave: ")
        if answer == "stay":
            if gold < level * 5:
                print("You don't have enough gold.")
            else:
                gold -= level * 5
                hp = maxhp
                hpCheck()
                print("Your HP was restored!")
    """
    def stay(self, player):
        # player should come here for free if game over
        if player.get_hp() <= 0:
            player.heal_full()
        else
    # maybe method for coming here after game over...? or should that be for player?
    # maybe include game over boolean