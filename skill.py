"""
Class for skills

Skills have MP cost, power, element, and effect
maybe also type and hits
0 power skills don't do any damage
Skills use magic to deal damage, and work based on defense
"""
import element
from status_effect import *
from entity import *
from random import *
from enum import *

DAMAGE = "Damaging"
HEAL = "Heal"
STATUS_EFFECT = "Effect"
class Skill:
    __slots__ = ["__name", "__cost", "__power", "__element", "__effect", "__hits", "__category", "__target_self"]
    def __init__(self, name, cost, power, element=element.NONE, effect=None, hits=1, category=DAMAGE, target_self = False):
        self.__name = name
        self.__cost = cost
        self.__power = power
        self.__element = element
        self.__effect = effect
        self.__hits = hits
        self.__category = category
        self.__target_self = target_self

    def __repr__(self):
        return self.__name + \
        "\n   Cost = " + str(self.__cost) + \
        "\n   Power = " + str(self.__power) + \
        "\n   Element = " + str(self.__element) + \
        "\n   Effect = " + str(self.__effect) + \
        "\n   Hits = " + str(self.__hits) + \
        "\n   Category = " + str(self.__category) + \
        "\n   Targets Self? = " + str(self.__target_self)
    def __str__(self):
        return self.__name
    def __hash__(self):
        return hash(self.__name)

    def use(self, entity):
        if self.__category == DAMAGE: # damaging skills deal magic damage
            power = 0
            for _ in range(self.__hits):
                power += self.__power + randint(0,5) # should add a way in the attack method to use external damage (or handle in use skill)
            if self.__effect is not None:
                entity.set_effect(self.__effect)
            return power
        
        elif self.__category == HEAL:
            heal = 0
            for _ in range(self.__hits):
                heal += self.__power + randint(0,5) # should add a way in the attack method to use external damage (or handle in use skill)
            if self.__effect is not None:
                duration = randint(3, 5)
                entity.set_effect(self.__effect, duration)
            return heal
        elif self.__category == STATUS_EFFECT:
            # maybe if element matches the user's element, the duration is boosted
            success = True
            if self.__effect is not None:
                if randint(1, 100) > 5: 
                    entity.set_effect(self.__effect) # should there be a chance of failure
                else:
                    success = False
            return success

    def get_name(self):
        return self.__name
    def get_cost(self):
        return self.__cost
    def get_power(self):
        return self.__power
    def get_element(self):
        return self.__element
    def get_effect(self):
        return self.__effect
    def get_hits(self):
        return self.__hits
    def get_target(self):
        return self.__target_self

    def reverse_target(self):
        self.__target_self = not self.__target_self

class SkillList(Enum):
    WEAKEN_FOE = Skill("Weaken Foe", 5, 0, element.NONE, StatusEffect.WEAKEN, 1, STATUS_EFFECT)
    DECAY_FOE = Skill("Decay Foe", 5, 0, element.NONE, StatusEffect.DECAY, 1, STATUS_EFFECT)
    DISQUIET_FOE = Skill("Disquiet Foe", 5, 0, element.NONE, StatusEffect.DISQUIET, 1, STATUS_EFFECT)
    SLOW_FOE = Skill("Slow Foe", 5, 0, element.NONE, StatusEffect.SLOW, 1, STATUS_EFFECT)
    POISON_FOE = Skill("Poison Foe", 10, 0, element.NONE, StatusEffect.POISON, 1, STATUS_EFFECT)
    DRAIN_FOE = Skill("Drain Foe", 10, 0, element.NONE, StatusEffect.DRAIN, 1, STATUS_EFFECT)
    FREEZE_FOE = Skill("Freeze Foe", 15, 0, element.NONE, StatusEffect.FREEZE, 1, STATUS_EFFECT)
    # Positive - maybe there should also be a variable declaring target
    STRENGTHEN_SELF = Skill("Strengthen Self", 5, 0, element.NONE, StatusEffect.STRENGTHEN, 1, STATUS_EFFECT)
    FORTIFY_SELF = Skill("Fortify  Self", 5, 0, element.NONE, StatusEffect.FORTIFY, 1, STATUS_EFFECT)
    EMPOWER_SELF = Skill("Empower Self", 5, 0, element.NONE, StatusEffect.EMPOWER, 1, STATUS_EFFECT)
    HASTEN_SELF = Skill("Hasten Self", 5, 0, element.NONE, StatusEffect.HASTEN, 1, STATUS_EFFECT)
    REGENERATE_SELF = Skill("Regenerate Self", 10, 0, element.NONE, StatusEffect.REGENERATE, 1, STATUS_EFFECT)
    FOCUS_SELF = Skill("Focus Self", 10, 0, element.NONE, StatusEffect.FOCUS, 1, STATUS_EFFECT)
    SLIPPERY_SELF = Skill("Slip Self", 15, 0, element.NONE, StatusEffect.SLIPPERY, 1, STATUS_EFFECT)

    BIG_STRIKE = Skill("Big Strike", 5, 50, element.NONE, None, 1, DAMAGE) # might change skill calc to just use magic for power?
    MULTI_STRIKE = Skill("Multi Strike", 5, 20, element.NONE, None, 3, DAMAGE)

    HEAL = Skill("Heal", 5, 50, element.LIGHT, None, 1, HEAL) # side note, heal skills should target self

    WATER = Skill("Water", 5, 50, element.WATER, None, 1, DAMAGE)
    FIRE = Skill("Fire", 5, 50, element.FIRE, None, 1, DAMAGE)
    PLANT = Skill("Plant", 5, 50, element.PLANT, None, 1, DAMAGE)
    EARTH = Skill("Earth", 5, 50, element.EARTH, None, 1, DAMAGE)
    AIR = Skill("Air", 5, 50, element.AIR, None, 1, DAMAGE)
    LIGHTNING = Skill("Lightning", 5, 50, element.LIGHTNING, None, 1, DAMAGE)
    LIGHT = Skill("Light", 5, 50, element.LIGHT, None, 1, DAMAGE)
    DARK = Skill("Dark", 5, 50, element.DARK, None, 1, DAMAGE)