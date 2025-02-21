"""
Attempt at making a better version of RPGPython.
Author: Esther Arimoro
"""
from random import *
from element import *

# Defines the starting values of all the global variables in the code.
level = 0
exp = 0
gold = 0
hp = 10
maxhp = 10
attack = 5
defense = 5
speed = 5
sword = 0
shield = 0
armor = 0 # maybe make armor increases lower speed
castleKey = 0
answer = " "
victory = 0
monsterLevel = 0
monsterEXP = 0
monsterATK = 0
monsterDef = 0
monsterSPD = 0
monsterHP = 0
monsterDamage = 0
monsterStrength = 0
monsterType = 0
damage = 0
bubble = 2
expCharm = 0
silentBoots = 0
goldCharm = 0
luckyCharm = 0

# Is called to make sure gold never falls below 0.
def goldCheck():
    global gold
    if gold < 0:
        gold = 0

# Can be called to allow the player to check their information.
def checkStats():
    global hp
    global maxhp
    global attack
    global defense
    global speed
    global sword
    global shield
    global armor
    global exp
    global level
    global gold
    global bubble
    global luckyCharm
    global goldCharm
    global expCharm
    global silentBoots
    
    # Shows numerical stats.
    print("Level", level)
    print("EXP:", exp)
    print("Amount to next level:", (level * 25) - exp)
    print(hp, "/", maxhp, "HP")
    print("Gold:", gold)
    print("Attack:", attack)
    print("Defense:", defense)
    print("Speed:", speed)
    print("Sword:", sword)
    print("Shield:", shield)
    print("Armor:", armor)
    
    # Shows which items are active.
    if bubble != 2:
        if bubble == 0:
            print("Bubble is inactive.")
        else:
            print("Bubble is active.")
    if luckyCharm == 1:
        print("Lucky Charm is active.")
    if goldCharm == 1:
        print("Gold Charm is active.")    
    if expCharm == 1:
        print("EXP Charm is active.")
    if silentBoots == 1:
        print("Silent Boots are active.")
        
# Is called to make sure that hp never exceeds maxhp, also making sure it never falls below 0.
def hpCheck():
    global hp
    global maxhp
    if hp > maxhp:
        hp = maxhp
    if hp < 0:
        hp = 0

# Level up handling; adds stats to the player upon level up.
def statCheck():
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global level
    global sword
    global armor
    global shield
    attack += 1
    defense += 1
    speed += 1
    hp += level
    maxhp += level
    hpCheck()

# Level up handling.
def levelUp():
    global level
    global exp
    if exp >= level * 25:
        # Levels the player up when their experience is more than 25 times the player's current level.
        exp = 0
        level += 1
        print("You leveled up! You're now at Level", level)
        statCheck()
# Shop handling.
def shop():
    global gold
    global shield
    global sword
    global armor
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global answer
    global bubble
    global expCharm
    global silentBoots
    global goldCharm
    global luckyCharm
    
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

# Dragon King's Castle Shop handling:
def dragonShop():
    global gold
    global shield
    global sword
    global armor
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global answer
    global bubble
    global expCharm
    global silentBoots
    global goldCharm
    global luckyCharm
    otherAnswer = "yes"
    # Shows the current amount of gold.
    print("Gold:", gold)
    
    # Greeting upon entering the store.
    print("The creature by the shop greets you warmly. What do you want to buy?")
    while otherAnswer == "yes" or otherAnswer == "Yes":
        answer = input("Sword upgrade, shield upgrade, armor upgrade, or items? ")
        # Invalid answer handling.
        while answer != "sword" and answer != "shield" and answer != "armor" and answer != "Sword" and answer != "Shield" and answer != "Armor" and answer != "sword upgrade" and answer != "shield upgrade" and answer != "armor upgrade" and answer != "Sword Upgrade" and answer != "Shield Upgrade" and answer != "Armor Upgrade" and answer != "Sword upgrade" and answer != "Shield upgrade" and answer != "Armor upgrade" and answer != "sword Upgrade" and answer != "shield Upgrade" and answer != "armor Upgrade" and answer != "items" and answer != "Items" and answer != "Nothing" and answer != "nothing":
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
        # Alternate "no thank you" answers
        if answer == "Nothing" or answer == "no thanks" or answer == "no" or answer == "No thanks" or answer == "No" or answer == "No Thanks":
            answer = "nothing"
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
        print("Gold:", gold)
        otherAnswer = input("Anything else? ")
        while otherAnswer != "Yes" and otherAnswer != "yes" and otherAnswer != "No" and otherAnswer != "no":
            print(otherAnswer, "is an invalid answer.")
            otherAnswer = input("Anything else? ")

# Induces a gameover.
def gameover():
    global exp
    global hp
    global gold
    if hp == 0:
        lostGold = randint(level, level * 3)
        gold -= lostGold
        goldCheck()
        print("You faint, losing", lostGold, "gold!")
        inn()

# Inn handling
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

# Hero's turn handling.
def heroTurn():
    global gold
    global shield
    global sword
    global armor
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global answer
    global exp
    global level
    global monsterLevel
    global monsterEXP
    global monsterHP
    global monsterATK
    global monsterDef
    global monsterSPD
    global monsterDamage
    global damage
    global luckyCharm
    if randint(1, 100) > 100 - sword or (luckyCharm == 1 and randint(1, 100) > 100 - (sword * 2)) :
        damage += 5
        print("Oh! A critical hit!")
    monsterHP -= damage
    if level <= 100:
        print("You dealt", damage, "damage to the monster!")
    else:
        print("You dealt", damage, "damage to the Dragon King!")
    
def monsterTurn():
    global hp
    global level
    global monsterDamage
    global answer
    global monsterATK
    global defense
    global bubble
    global monsterStrength
    global gold
    if bubble == 1:
        print("Your protective bubble took the hit!")
        print("Your bubble burst!")
        bubble = 0
    else:
        if answer == "defend":
            if randint(1, 10) < 10:
                monsterDamage = monsterATK + randint(0, 5) - (defense * 2)
                if monsterDamage < 1:
                    monsterDamage = 1
            else:
                print("The monster broke through your defense!")
        hp -= monsterDamage
        if level < 100:
            print("The monster attacks, dealing", monsterDamage, "damage to you!")
            if monsterStrength == 4:
                droppedGold = randint(1, 5)
                print("The monster dropped", droppedGold, "gold!")
                gold += droppedGold
        else:
            print("The Dragon King attacks, dealing", monsterDamage, "damage to you!")
        hpCheck()
    
def fight():
    global gold
    global shield
    global sword
    global armor
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global answer
    global exp
    global level
    global monsterLevel
    global monsterEXP
    global monsterHP
    global monsterATK
    global monsterDef
    global monsterSPD
    global monsterDamage
    global monsterStrength
    global damage
    global bubble
    global expCharm
    global silentBoots
    global goldCharm
    global luckyCharm
    checkStats()
    print("You head into the wilderness.")
    answer = input("Continue further, turn back: ")
    if answer == "Continue" or answer == "Fight":
        answer = "continue"
    elif answer == "Turn Back" or answer == "Turn" or answer == "turn" or answer == "back" or answer == "Back":
        answer = "turn back"
    while answer != "continue" and answer != "turn back": 
        print(answer, "is an invalid answer.")
        answer = input("Continue further, turn back: ")
        if answer == "Continue" or answer == "Fight":
            answer = "continue"
        elif answer == "Turn Back" or answer == "Turn" or answer == "turn" or answer == "back" or answer == "Back":
            answer = "turn back"
    while answer == "continue":
        if randint(1, 5) > 2:
            if bubble != 2:
                bubble = 1
            monsterLevel = level + randint(-2, 2)
            if monsterLevel < 1:
                monsterLevel = 1
            monsterStrengthChoose = randint(1, 100)
            if monsterStrengthChoose >= 99:
                monsterStrength = 4
            elif monsterStrengthChoose >= 70:
                monsterStrength = 1
            elif monsterStrengthChoose >= 15:
                monsterStrength = 2
            elif monsterStrengthChoose >= 1:
                monsterStrength = 3
            if monsterStrength == 1:
                monsterHP = monsterLevel * 4 + randint(-(monsterLevel), 3)
                monsterEXP = monsterLevel * 4
                if level < 30:
                    monsterATK = monsterLevel * 2 + randint(-3, 3) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 2 + randint(-3, 3) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 2 + randint(-3, 3)
                elif level < 70 and level > 29:
                    monsterATK = monsterLevel * 5 + randint(-3, 6) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 5 + randint(-3, 6) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 5 + randint(-3, 6)
                else:
                    monsterATK = monsterLevel * 10 + randint(-3, 11) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 10 + randint(-3, 11) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 10 + randint(-3, 11)
                    
            elif monsterStrength == 2:
                monsterHP = monsterLevel * 5 + randint(-(monsterLevel), 3)
                monsterEXP = monsterLevel * 5
                if level < 30:
                    monsterATK = monsterLevel * 3 + randint(-3, 3) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 3 + randint(-3, 3) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 3 + randint(-3, 3)
                elif level < 70 and level > 29:
                    monsterATK = monsterLevel * 6 + randint(-3, 6) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 6 + randint(-3, 6) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 6 + randint(-3, 6)
                else:
                    monsterATK = monsterLevel * 11 + randint(-3, 11) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 11 + randint(-3, 11) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 11 + randint(-3, 11)
            elif monsterStrength == 3 or monsterStrength == 4:
                monsterHP = monsterLevel * 6 + randint(-(monsterLevel), 3)
                monsterEXP = monsterLevel * 6
                if level > 30:
                    monsterATK = monsterLevel * 4 + randint(-3, 3) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 4 + randint(-3, 3) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 4 + randint(-3, 3)
                elif level > 70 and level > 29:
                    monsterATK = monsterLevel * 7 + randint(-3, 6) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 7 + randint(-3, 6) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 7 + randint(-3, 6)
                else:
                    monsterATK = monsterLevel * 12 + randint(-3, 11) + (sword * randint(-1, 1))
                    monsterDef = monsterLevel * 12 + randint(-3, 11) + (shield * randint(-1, 1))
                    monsterSPD = monsterLevel * 12 + randint(-3, 11)
            print("You encounter a Level", monsterLevel, "monster!")
            if monsterStrength == 1:
                print("It seems weaker than average...")
            elif monsterStrength == 3:
                print("It seems stronger than average!")
            elif monsterStrength == 4:
                print("Oh! A gold monster!")
            while monsterHP > 0:
                answer = input("Fight; Flee; Check Stats; or Defend: ")
                if answer == "Fight" or answer == "Battle" or answer == "battle":
                    answer = "fight"
                elif answer == "Flee" or answer == "Escape" or answer == "escape":
                    answer = "flee"
                elif answer == "Check Stats" or answer == "Stats" or answer == "Check" or answer == "stat" or answer == "Stat":
                    answer = "check stats"
                elif answer == "Defend" or answer == "guard" or answer == "Guard":
                    answer = "defend"
                while answer != "fight" and answer != "defend" and answer != "flee" and answer != "check stats" and answer != "stats" and answer != "check": 
                    print(answer, "is an invalid answer.")
                    answer = input("Fight; Flee; Check Stats; or Defend: ")
                    if answer == "Fight" or answer == "Battle" or answer == "battle":
                        answer = "fight"
                    elif answer == "Flee" or answer == "Escape" or answer == "escape":
                        answer = "flee"
                    elif answer == "Check Stats" or answer == "Stats" or answer == "Check" or answer == "stat" or answer == "Stat":
                        answer = "check stats"
                    elif answer == "Defend" or answer == "guard" or answer == "Guard":
                        answer = "defend"
                damage = attack + randint(0, 5) - monsterDef
                if damage < 1:
                    damage = 1
                monsterDamage = monsterATK + randint(0, 5) - defense
                if monsterDamage < 1:
                    monsterDamage = 1
                if answer == "fight":
                    if speed > monsterSPD:
                        heroTurn()
                        if monsterHP > 0:
                            monsterTurn()
                            if hp <= 0:
                                gameover()
                                break
                    else:
                        monsterTurn()
                        if hp <= 0:
                            gameover()
                            break
                        else:
                            heroTurn()    
                elif answer == "defend":
                    monsterDamage = monsterATK + randint(0, 5) - defense
                    if monsterDamage < 1:
                        monsterDamage = 1
                    print("You defend against the monster!")
                    if randint(1, 100) > 50 + shield:
                        if randint(0, 10 * level) < 1 + shield:
                            print("You blocked all damage!")
                        else:
                            monsterTurn()
                            if hp <= 0:
                                gameover()
                                break
                    else:
                        monsterTurn()    
                        if hp <= 0:
                            gameover()
                            break
                elif answer == "flee":
                    if (speed > monsterSPD and (randint(1, 5) != 1 or silentBoots == 1)) or (randint(1, 5) <= 2 or (silentBoots == 1 and randint(1, 9) < 10)):
                        print("You fled from the battle!")
                        break
                    else:
                        monsterDamage = monsterATK + randint(0, 5) - defense
                        if monsterDamage < 1:
                            monsterDamage = 1
                        print("You failed to escape!")
                        monsterTurn()
                        if hp <= 0:
                            gameover()
                            break
                elif answer == "check stats" or answer == "stats" or answer == "check":
                    checkStats()
            if monsterHP <= 0:
                print("You've slain the monster!")
                if monsterStrength != 4:
                    if monsterStrength != 3:
                        if expCharm == 0:
                            monsterEXP = monsterLevel * randint(1, 5)
                        else:
                            monsterEXP = monsterLevel * randint(2, 10)
                    else:
                        if expCharm == 0:
                            monsterEXP = (monsterLevel * randint(1, 5)) + monsterLevel
                        else:
                            monsterEXP = (monsterLevel * randint(2, 10)) + (monsterLevel * 2)
                    if goldCharm == 0:
                        monsterGold = monsterLevel * randint(1, 5)
                    else:
                        monsterGold = monsterLevel * randint(2, 10)
                else:
                    if expCharm == 0:
                        monsterEXP = monsterLevel * randint(1, 5) + monsterStrength
                    else:
                        monsterEXP = monsterLevel * randint(2, 10) + (monsterStrength * 2)
                    if goldCharm == 0:
                        monsterGold = monsterLevel * randint(7, 10) + monsterStrength
                    else:
                        monsterGold = monsterLevel * randint(7, 14) + (monsterStrength * 2)
                print("You earned", monsterEXP, "EXP and", monsterGold, "gold!")
                exp += monsterEXP
                gold += monsterGold
                levelUp()
        else:
            if level > 100:
                break
            if randint(1, 20) < 2:
                print("You encounter a healing spot!")
                if randint(1,5) > 1:
                    hp += 10
                    hpCheck()
                    print("Your HP was restored by 10 points!")
                else:
                    hp = maxhp
                    hpCheck()
                    print("Your HP was fully restored!")
            elif randint(1, 20) < 2:
                foundGold = randint(1, 1 + (5 * level))
                print("You find", foundGold, "gold on the ground!")
                gold += foundGold
            elif randint(1, 100) <= 5:
                print("You find a treasure chest!")
                treasureFound = randint(1, 3)
                if treasureFound == 1:    
                    print("You found an Attack Brew! Attack is up by", level)
                    attack += level
                elif treasureFound == 2:
                    print("You found a Defense Brew! Defense is up by", level)
                    defense += level
                else:
                    print("You found a Speed Brew! Speed is up by", level)
                    speed += level
            else:
                print("You encounter nothing. Head back?")
            answer = input("Continue further, turn back: ")
            if answer == "Continue" or answer == "Fight":
                answer = "continue"
            elif answer == "Turn Back" or answer == "Turn" or answer == "turn" or answer == "back" or answer == "Back":
                answer = "turn back"
            while answer != "continue" and answer != "turn back": 
                print(answer, "is an invalid answer.")
                answer = input("Continue further, turn back: ")
                if answer == "Continue" or answer == "Fight":
                    answer = "continue"
                elif answer == "Turn Back" or answer == "Turn" or answer == "turn" or answer == "back" or answer == "Back":
                    answer = "turn back"
            if answer == "turn back":
                print("You head back to the village.")
        while answer != "continue" and answer != "turn back": 
            print(answer, "is an invalid answer.")
            answer = input("Continue further, turn back: ")
            if answer == "Continue" or answer == "Fight":
                answer = "continue"
            elif answer == "Turn Back" or answer == "Turn" or answer == "turn" or answer == "back" or answer == "Back":
                answer = "turn back"
        if answer == "turn back":
            print("You head back to the village.")

# Final battle handling.
def dragon():
    global gold
    global shield
    global sword
    global armor
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global answer
    global victory
    global exp
    global level
    global monsterLevel
    global monsterEXP
    global monsterHP
    global monsterATK
    global monsterDef
    global monsterSPD
    global monsterDamage
    global damage
    global bubble
    global expCharm
    global silentBoots
    global goldCharm
    global luckyCharm
    statCheck()
    checkStats()
    print("You enter the Dragon King's castle.")
    print("A shopkeeper awaits just before the entrance to the King's lair.")
    if gold < 25:
        print("The shopkeep notices your lack of money. Out of the goodness of its heart, it gives you enough for a few potions.")
        gold += 50
    dragonShop()
    print("You enter the Dragon King's lair.")
    monsterLevel = 100
    monsterHP = monsterLevel * 300
    monsterATK = monsterLevel * 15
    monsterDef = monsterLevel * 2
    monsterSPD = monsterLevel * 15
    print("The Level 100 Dragon King attacks!")
    while monsterHP > 0:
        answer = input("Fight, Defend, or check stats?: ")
        if answer == "Fight" or answer == "Battle" or answer == "battle":
            answer = "fight"
        elif answer == "Check Stats" or answer == "Stats" or answer == "Check" or answer == "stat" or answer == "Stat":
            answer = "check stats"
        elif answer == "Defend" or answer == "guard" or answer == "Guard":
            answer = "defend"
        while answer != "fight" and answer != "defend" and answer != "check stats" and answer != "stats" and answer != "check": 
            if answer == "flee" or answer == "Flee" or answer == "Escape" or answer == "escape":
                print("There is no fleeing this fight!")
            else:
                print(answer, "is an invalid answer.")
            answer = input("Fight; or Defend: ")
            if answer == "Fight" or answer == "Battle" or answer == "battle":
                answer = "fight"
            elif answer == "Check Stats" or answer == "Stats" or answer == "Check" or answer == "stat" or answer == "Stat":
                answer = "check stats"
            elif answer == "Defend" or answer == "guard" or answer == "Guard":
                answer = "defend"
        damage = attack + randint(0, 5) - monsterDef
        if defense <= 1000:
            monsterDamage = monsterATK + randint(0, 50) - defense + randint(0, 50)
        else:
            monsterDamage = monsterATK + randint(0, 50) - 1000 + randint(0, 50)
        
        if answer == "fight":
            if speed > monsterSPD:
                heroTurn()
                if monsterHP <= 0:
                    print("You've slain the Dragon King!")
                    victory = 1
                    break
                else:
                    if defense > 1000:
                        print("The Dragon King pierces through your high defenses!")
                    monsterTurn()
                    if hp <= 0:
                        victory = -1
                        hp = maxhp
                        print("You fall, but the thought of the village is enough for you to keep on fighting!")
                        dragon()
                        break
            else:
                monsterTurn() # maybe add a chance to heal damage
                if hp <= 0:
                    victory = -1
                    hp = maxhp
                    print("You fall, but the thought of the village is enough for you to keep on fighting!")
                    dragon()
                    break
                else:
                    heroTurn()
        elif answer == "defend":
            monsterDamage = monsterATK + randint(0, 50) - defense
            print("You defend against the Dragon King!")
            if randint(1, 100) > 50 + shield:
                if randint(0, 10 * level) > 1 + shield:
                    print("You blocked all damage!")
                else:
                    monsterTurn()
                    if hp <= 0:
                        victory = -1
                        hp = maxhp
                        print("You fall, but the thought of the village is enough for you to keep on fighting!")
                        dragon()
                        break
            else:
                monsterTurn()    
                if hp <= 0:
                    victory = -1
                    hp = maxhp
                    print("You fall, but the thought of the village is enough to revive you!")
                    dragon()
                    break
        elif answer == "check stats" or answer == "stats" or answer == "check":
            checkStats()
        if monsterHP <= 0:
            print("You've slain the Dragon King!")
            victory = 1
            break

# Debug stuff
def devCheats():
    global gold
    global shield
    global sword
    global armor
    global attack
    global defense
    global speed
    global hp
    global maxhp
    global answer
    global victory
    global exp
    global level
    global monsterLevel
    global monsterEXP
    global monsterHP
    global monsterATK
    global monsterDef
    global monsterSPD
    global monsterDamage
    global damage
    global bubble
    global expCharm
    global silentBoots
    global goldCharm
    global luckyCharm
    print("You enter the Development Room. Rows of buttons and screens face you.")
    while answer != "exit":
        checkStats()
        answer = input("Edit which value?: ")
        if answer == "gold":
            print("Gold is currently", gold, "gold.")
            gold = int(input("Set a new value for gold: "))
            goldCheck()
        if answer == "exp":
            print("EXP is currently", exp, "EXP.")
            exp += int(input("Add how much to EXP?: "))
            levelUp()
        if answer == "level":
            print("Level is currently LVL", level, ".")
            level = int(input("Set level to what?: "))
        if answer == "shield":
            print("Shield level is currently LV", shield, ".")
            shield = int(input("Set shield level to what?: "))
        if answer == "sword":
            print("Sword level is currently LV", sword, ".")
            sword = int(input("Set sword level to what?: "))
        if answer == "armor":
            print("Armor level is currently LV", armor, ".")
            armor = int(input("Set armor level to what?: "))
        if answer == "attack":
            print("Attack is currently", attack, ".")
            attack = int(input("Set attack to what?: "))
        if answer == "defense":
            print("Defense is currently", defense, ".")
            defense = int(input("Set defense to what?: "))
        if answer == "speed":
            print("Speed is currently", speed, ".")
            speed = int(input("Set speed to what?: "))
        if answer == "maxhp":
            print("Max HP is currently", maxhp, ".")
            maxhp = int(input("Set Max HP to what?: "))
            hpCheck()
        if answer == "hp":
            print("HP is currently", hp, ".")
            hp = int(input("Set HP to what?: "))
            hpCheck()
        if answer == "bubble":
            if bubble > 1:
                print("The protective bubble is currently disabled.")
            elif bubble <= 1:
                print("The protective bubble is currently enabled.")
            answer = input("Change bubble status (true/false)?: ")
            if answer == "true" or answer == "True":
                bubble = 1
                print("The protective bubble is currently enabled.")
            if answer == "false" or answer == "False":
                bubble = 2
                print("The protective bubble is currently disabled.")
        if answer == "exp charm":
            if expCharm == 0:
                print("The EXP Charm is currently disabled.")
            elif expCharm == 1:
                print("The EXP Charm is currently enabled.")
            answer = input("Change EXP Charm status (true/false)?: ")
            if answer == "true" or answer == "True":
                expCharm = 1
                print("The EXP Charm is currently enabled.")
            if answer == "false" or answer == "False":
                expCharm = 0
                print("The EXP Charm is currently disabled.")
        if answer == "gold charm":
            if goldCharm == 0:
                print("The Gold Charm is currently disabled.")
            elif goldCharm == 1:
                print("The Gold Charm is currently enabled.")
            answer = input("Change Gold Charm status (true/false)?: ")
            if answer == "true" or answer == "True":
                goldCharm = 1
                print("The Gold Charm is currently enabled.")
            if answer == "false" or answer == "False":
                goldCharm = 0
                print("The Gold Charm is currently disabled.")
        if answer == "lucky charm":
            if luckyCharm == 0:
                print("The Lucky Charm is currently disabled.")
            elif luckyCharm == 1:
                print("The Lucky Charm is currently enabled.")
            answer = input("Change Lucky Charm status (true/false)?: ")
            if answer == "true" or answer == "True":
                luckyCharm = 1
                print("The Lucky Charm is currently enabled.")
            if answer == "false" or answer == "False":
                luckyCharm = 0
                print("The Lucky Charm is currently disabled.")
        if answer == "silent boots":
            if silentBoots == 0:
                print("The Silent Boots are currently disabled.")
            elif silentBoots == 1:
                print("The Silent Boots are currently enabled.")
            answer = input("Change Silent Boots status (true/false)?: ")
            if answer == "true" or answer == "True":
                silentBoots = 1
                print("The Silent Boots are currently enabled.")
            if answer == "false" or answer == "False":
                silentBoots = 0
                print("The Silent Boots are currently disabled.")

while level <= 100 or victory == -1:
    print("You arrive at the village! What will you do?")
    answer = input("Go to the shop, go fight monsters, go to inn: ")
    if answer == "leave" or answer == "Leave" or answer == "Fight":
        answer = "fight"
    elif answer == "Shop" or answer == "Buy" or answer == "buy":
        answer = "shop"
    elif answer == "Inn" or answer == "Rest" or answer == "rest":
        answer = "inn"
    while answer != "shop" and answer != "fight" and answer != "inn" and answer != "dev cheats":
        print(answer, "is an invalid answer.")
        answer = input("Go to the shop, go fight monsters, go to inn: ")
        if answer == "leave" or answer == "Leave" or answer == "Fight":
            answer = "fight"
        elif answer == "Shop" or answer == "Buy" or answer == "buy":
            answer = "shop"
        elif answer == "Inn" or answer == "Rest" or answer == "rest":
            answer = "inn"
    if answer == "shop":
        shop()
    elif answer == "fight":
        fight()
    elif answer == "inn":
        inn()
    elif answer == "dev cheats":
        devCheats()
    if level > 100:
        print("You've earned enough Levels to challenge the evil Dragon King!")
        dragon()
        if victory == 1:
            break
if victory == 1:
    print("Congradulations!")
    print("You freed the village from the evil Dragon King!")