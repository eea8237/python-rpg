package java_rpg.other;

public enum Option {
    FIGHT("Fight"),
    DEFEND("Defend"),
    ITEM("Items"),
    SKILL("Skills"),
    FLEE("Flee"),

    private final String name;

    private Option(String name) {
        this.name = name;
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
