package java_rpg.other;

import java.util.*;

public enum Element {
    NONE("Colorless"),
    WATER("Blue"),
    FIRE("Red"),
    PLANT("Green"),
    EARTH("Brown"),
    AIR("White"),
    LIGHTNING("Yellow"),
    LIGHT("Bright"),
    DARK("Night"),
    ALL("Prism");

    private final String name;
    private Set<Element> resistances;
    private Set<Element> weaknesses;
    private Element(String name) {
        this.name = name;
    }

    /*
     * Set weaknesses and resistances at the start of the game
     */
    public static void initWeaknesses() {
        NONE.weaknesses = new HashSet<>();
        WATER.weaknesses = new HashSet<>(PLANT);
        FIRE.weaknesses = new HashSet<>(WATER);
        PLANT.weaknesses = new HashSet<>(FIRE);
        EARTH.weaknesses = new HashSet<>(AIR);
        AIR.weaknesses = new HashSet<>(LIGHTNING);
        LIGHTNING.weaknesses = new HashSet<>(EARTH);
        LIGHT.weaknesses = new HashSet<>(DARK);
        DARK.weaknesses = new HashSet<>(LIGHT);
        ALL.weaknesses = new HashSet<>();
    }
    public static void initResistances() {
        NONE.resistances = new HashSet<>();
        WATER.resistances = new HashSet<>(FIRE);
        FIRE.resistances = new HashSet<>(PLANT);
        PLANT.resistances = new HashSet<>(WATER);
        EARTH.resistances = new HashSet<>(LIGHTNING);
        AIR.resistances = new HashSet<>(EARTH);
        LIGHTNING.resistances = new HashSet<>(AIR);
        LIGHT.resistances = new HashSet<>(EARTH, AIR, LIGHTNING);
        DARK.resistances = new HashSet<>(WATER, FIRE, PLANT);
        ALL.resistances = new HashSet<>(ALL);
    }

    /**
     * @param other another element
     * @return true if this element is weak to the other element, false otherwise.
     */
    public boolean isWeakTo(Element other) {
        // none is weak to every element except none
        if (this.equals(NONE) && !other.equals(NONE)) {
            return true;
        } else {
            return this.weaknesses.contains(other);
        }
    }

    /**
     * @param other another element
     * @return true if this element resists the other element, false otherwise.
     */
    public boolean resists(Element other) {
        // none is resisted by every element except none
        if (other.equals(NONE) && !this.equals(NONE)) {
            return true;
        } else {
            return this.resistances.contains(other);
        }
    }

    @Override
    public String toString() {
        return this.name;
    };

    @Override
    public int hashCode() {
        return this.name.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Stat other) {
            return this.name.equals(other.name);
        } else {
            return false;
        }
    }
}
