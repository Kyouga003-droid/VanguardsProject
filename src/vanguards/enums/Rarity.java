package vanguards.enums;

import java.awt.Color;

public enum Rarity {
    COMMON(Color.LIGHT_GRAY, 1.0, "Common", 10),
    RARE(new Color(0, 150, 255), 1.8, "Rare", 25),
    EPIC(new Color(180, 50, 255), 3.0, "Epic", 75),
    LEGENDARY(new Color(255, 180, 0), 5.5, "Legendary", 200),
    MYTHIC(new Color(255, 50, 150), 9.0, "Mythical", 500),
    GODLY(new Color(0, 255, 200), 16.0, "Godly", 1500);

    public final Color col; 
    public final double multiplier; 
    public final String name; 
    public final int sellValue;
    
    Rarity(Color c, double m, String n, int sv) { 
        col = c; multiplier = m; name = n; sellValue = sv; 
    }
}
