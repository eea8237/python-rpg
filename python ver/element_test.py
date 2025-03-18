import element

"""
effectiveness
"""
def test_effective_Water_Fire():
    # setup
    element1 = element.WATER
    element2 = element.FIRE
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Fire_Plant():
    # setup
    element1 = element.FIRE
    element2 = element.PLANT
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Plant_Water():
    # setup
    element1 = element.PLANT
    element2 = element.WATER
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Earth_Lightning():
    # setup
    element1 = element.EARTH
    element2 = element.LIGHTNING
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Air_Earth():
    # setup
    element1 = element.AIR
    element2 = element.EARTH
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Lightning_Air():
    # setup
    element1 = element.LIGHTNING
    element2 = element.AIR
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Light_Dark():
    # setup
    element1 = element.LIGHT
    element2 = element.DARK
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Dark_Light():
    # setup
    element1 = element.DARK
    element2 = element.LIGHT
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Fire_Earth():
    # setup
    element1 = element.FIRE
    element2 = element.EARTH
    expected = False

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Fire_Water():
    # setup
    element1 = element.FIRE
    element2 = element.WATER
    expected = False

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_None_Earth():
    # setup
    element1 = element.NONE
    element2 = element.EARTH
    expected = False

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Earth_None():
    # setup
    element1 = element.EARTH
    element2 = element.NONE
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

"""
resisted
"""
def test_resisted_Fire_Water():
    # setup
    element1 = element.FIRE
    element2 = element.WATER
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Plant_Fire():
    # setup
    element1 = element.PLANT
    element2 = element.FIRE
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Water_Plant():
    # setup
    element1 = element.WATER
    element2 = element.PLANT
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Lightning_Earth():
    # setup
    element1 = element.LIGHTNING
    element2 = element.EARTH
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Earth_Air():
    # setup
    element1 = element.EARTH
    element2 = element.AIR
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Air_Lightning():
    # setup
    element1 = element.AIR
    element2 = element.LIGHTNING
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Earth_Light():
    # setup
    element1 = element.EARTH
    element2 = element.LIGHT
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Air_Light():
    # setup
    element1 = element.AIR
    element2 = element.LIGHT
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Lightning_Light():
    # setup
    element1 = element.LIGHTNING
    element2 = element.LIGHT
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Fire_Dark():
    # setup
    element1 = element.FIRE
    element2 = element.DARK
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Water_Dark():
    # setup
    element1 = element.WATER
    element2 = element.DARK
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Plant_Dark():
    # setup
    element1 = element.PLANT
    element2 = element.DARK
    expected = True

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Dark_Light():
    # setup
    element1 = element.DARK
    element2 = element.LIGHT
    expected = False

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Fire_Earth():
    # setup
    element1 = element.FIRE
    element2 = element.EARTH
    expected = False

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_Water_Fire():
    # setup
    element1 = element.WATER
    element2 = element.FIRE
    expected = False

    # invoke
    actual = element1.resisted(element2)

    # analyze
    assert expected == actual

def test_resisted_None_Earth():
    # setup
    element1 = element.NONE
    element2 = element.EARTH
    expected = False

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual

def test_effective_Earth_None():
    # setup
    element1 = element.EARTH
    element2 = element.NONE
    expected = True

    # invoke
    actual = element1.effective(element2)

    # analyze
    assert expected == actual