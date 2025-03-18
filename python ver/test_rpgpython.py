import entity
import player
import monster

from status_effect import *
import skill
import element
import item
import potion
import charm
import armor

import world
import town
import wilds
import battle

def main():
    e1 = entity.Entity("E1", element.FIRE,[entity.FIGHT, entity.DEFEND], [skill.HEAL], None)
    e2 = entity.Entity("E2", element.WATER,[entity.FIGHT, entity.DEFEND, entity.SKILL], [skill.WEAKEN_FOE, skill.BIG_STRIKE], None)
    #p = player.Player(input("Enter name: "))
    p = player.Player()
    '''print(repr(e1))
    p.add_exp(25)
    print(repr(p))
    print(p.get_to_next_level())
    p.level_up()
    print(p.get_to_next_level())
    p.level_up()
    print(repr(p))
    print(p)'''
    s = town.Shop("Test")
    i = town.Inn("Test", 50)
    t = town.Town("Town", s, i)
    print(repr(t))
    t.interact(p)
    
    '''print(repr(e1))
    print(repr(e2))
    print(e1)
    e1.set_status(StatusEffect.WEAKEN, 5)
    e1.process_effect()
    print(repr(e1))'''
    '''print(e1.attack(e2))
    e2.defend()
    print(e1.attack(e2))
    print(e1.attack(e2))
    print(e1.attack(e2))
    print()
    print(repr(e1))
    print(repr(e2))
    e2.increase_HP(10)
    print(e2)

    print(e1.speed_check(e2))
    print(e1.speed_check(e2))
    print(e1.speed_check(e2))'''

if __name__ == "__main__":
    main()