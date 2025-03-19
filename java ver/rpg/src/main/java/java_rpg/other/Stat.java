package java_rpg.other;

public enum Stat {
    MAXHP("Max HP", 10),
    MAXMP("Max MP", 10),
    HP("HP", 10),
    MP("MP", 10),
    ATTACK("Attack"),
    DEFENSE("Defense"),
    MAGIC("Magic"),
    SPEED("Speed"),
    TEMP_ATTACK("Temp. ATK", 0),
    TEMP_DEFENSE("Temp. DEF", 0),
    TEMP_MAGIC("Temp. MAG", 0),
    TEMP_SPEED("Temp. SPD", 0),
    LEVEL("Level", 1),
    EXPERIENCE("EXP", 0),
    GOLD("Gold", 0);

    
    private final String name;
    private final int startingValue;
    
    /**
     * Initiallize stat with its name and starting value.
     * @param name
     * @param startingValue
     */
    private Stat(String name, int startingValue) {
        this.name = name;
        this.startingValue = startingValue;
    }

    /**
     * Initialize stat with a starting value of 5.
     * @param name
     */
    private Stat(String name) {
        this.name = name;
        this.startingValue = 5;
    }

    public String getName() {
        return this.name;
    }
    public int getStartingValue() {
        return this.startingValue;
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
