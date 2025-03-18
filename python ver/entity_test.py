import entity
import element
import skill
from status_effect import *

def test_entity_creation_default():
    # setup
    e = entity.Entity()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [None, 0]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_creation():
    # setup
    e = entity.Entity("Bob", element.AIR, ["Fight", "Flee"], [skill.AIR, skill.HEAL])
    e.set_status(StatusEffect.FORTIFY, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = Bob" + \
        "\n   Element = Air" + \
        "\n   Status = [Fortify, 5]" + \
        "\n   Options = ['Fight', 'Flee']" + \
        "\n   Skills = ['Air', 'Heal']" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [2.5, 5], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

"""
Effects
"""
def test_entity_weaken():
    e = entity.Entity()
    e.set_status(StatusEffect.WEAKEN, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Weaken, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [-2.5, 5], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_decay():
    e = entity.Entity()
    e.set_status(StatusEffect.DECAY, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Decay, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [-2.5, 5], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_disquiet():
    e = entity.Entity()
    e.set_status(StatusEffect.DISQUIET, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Disquiet, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [-2.5, 5], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_slow():
    e = entity.Entity()
    e.set_status(StatusEffect.SLOW, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Slow, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [-2.5, 5], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_poison():
    e = entity.Entity()
    e.set_status(StatusEffect.POISON, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Poison, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 9, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_poison_zero():
    e = entity.Entity()
    e.set_status(StatusEffect.POISON, 5)
    e.decrease_HP(10)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Poison, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 0, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_drain():
    e = entity.Entity()
    e.set_status(StatusEffect.DRAIN, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Sap, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 9, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_drain_zero():
    e = entity.Entity()
    e.set_status(StatusEffect.DRAIN, 5)
    e.decrease_MP(10)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Sap, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 0, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

# positive stats
def test_entity_strengthen():
    e = entity.Entity()
    e.set_status(StatusEffect.STRENGTHEN, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Strengthen, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [2.5, 5], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_fortify():
    e = entity.Entity()
    e.set_status(StatusEffect.FORTIFY, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Fortify, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [2.5, 5], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_empower():
    e = entity.Entity()
    e.set_status(StatusEffect.EMPOWER, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Empower, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [2.5, 5], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_hasten():
    e = entity.Entity()
    e.set_status(StatusEffect.HASTEN, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Hasten, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [2.5, 5], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_regenerate():
    e = entity.Entity()
    e.set_status(StatusEffect.REGENERATE, 5)
    e.decrease_HP(5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Regenerate, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 6, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_regenerate_full():
    e = entity.Entity()
    e.set_status(StatusEffect.REGENERATE, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Regenerate, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_focus():
    e = entity.Entity()
    e.set_status(StatusEffect.FOCUS, 5)
    e.decrease_MP(5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Focus, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 6, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

def test_entity_focus_full():
    e = entity.Entity()
    e.set_status(StatusEffect.FOCUS, 5)
    e.process_effect()
    expected = "Entity: " + \
        "\n   Name = None" + \
        "\n   Element = Nonelemental" + \
        "\n   Status = [Focus, 5]" + \
        "\n   Options = None" + \
        "\n   Skills = None" + \
        "\n   Stats = {'Max HP': 10, 'HP': 10, 'Max MP': 10, 'MP': 10, 'Attack': 5, 'Defense': 5, 'Magic': 5, 'Speed': 5, 'Temp. ATK': [0, 0], 'Temp. DEF': [0, 0], 'Temp. MAG': [0, 0], 'Temp. SPD': [0, 0], 'Level': 0, 'Gold': 0}"
    
    # invoke
    actual = repr(e)
    
    # analyze
    assert actual == expected

# test slippery later

# attack is random - test it later
# can test defend