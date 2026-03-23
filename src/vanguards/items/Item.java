package vanguards.items;

import vanguards.enums.Rarity;

public class Item {
    public String name;
    public int price; 
    public Rarity rarity;
    
    public Item(String n, int p, Rarity r) { 
        name = n; price = p; rarity = r; 
    }
}
