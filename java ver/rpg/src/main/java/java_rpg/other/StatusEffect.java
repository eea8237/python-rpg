package java_rpg.other;

public enum StatusEffect {
    NORMAL("Normal"),
    // negative
    WEAKEN("Weaken"), // lower attack
    DECAY("Decay"), // lower defense
    DISQUIET("Disquiet"), // lower mp
    SLOW("Slow"), // lower speed
    POISON("Poison"), // lose hp
    SAP("Sap"), // lose mp
    FREEZE("Freeze"), // lose a turn

    // positive
    STRENGTHEN("Strengthen"), // boost attack
    FORTIFY("Fortify"), // boost defense
    EMBOLDEN("Embolden"), // boost magic
    HASTEN("Hasten"), // boost speed
    REGENERATE("Regenerate"), // heal hp
    FOCUS("Focus"), // heal mp
    MELT("Melt"); // 2 consecutive turns

    private final String name;
    /**
     * How long the status effect lasts
     */
    private int duration;

    private StatusEffect(String name) {
        this.name = name;
        this.duration = 0;
    }

    public int getDuration() {
        return this.duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
        this.duration = this.duration < 0 ? 0 : this.duration;
    }

    public void incrementDuration() {
        this.duration++;
    }

    public void decrementDuration() {
        this.duration--;
        this.duration = this.duration < 0 ? 0 : this.duration;
    }

    public void resetDuration() {
        this.duration = 0;
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
