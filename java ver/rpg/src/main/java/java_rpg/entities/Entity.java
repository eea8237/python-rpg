package java_rpg.entities;

import java.util.*;

import java_rpg.other.*;
import java_rpg.items.*;
import java_rpg.skills.*;
import java_rpg.*;
/**
 * Class for an entity (a player or monster)
 */
public abstract class Entity {
    protected final String name;
    protected final Map<Stat, Integer> stats;
    protected Element element;
    protected final Set<Option> options;
    protected StatusEffect status;
    protected final HashMap<String, Item> items;

    public Entity(String name, Map<Stat, Integer> stats, Element element, Set<Option> options, StatusEffect status, Set<Item> items) {
        this.name = name;
        this.element = element;
        this.stats = stats;
        this.items = items;
        this.options = options;
        this.status = status;
    }
    // create other defaults
    // create an entity with only a name
    public Entity(String name) {
        this.name = name;
        
        this.stats = new HashMap<>();
        for (Stat stat : Stat.values()) {
            this.stats.put(stat, stat.getStartingValue())
        }
        
        this.element = Element.None;
        this.items = new HashMap<>();
        this.options = new Set<Option>();
        this.status = StatusEffect.Normal;
    }

}
