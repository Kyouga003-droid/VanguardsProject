package vanguards.enums;

import java.awt.Color;

public enum ClassType {
    KNIGHT("Knight", "Scales with: MAX HP & DEF", new Color(40, 70, 130), new Color(15, 25, 45)),
    SORCERER("Sorcerer", "Scales with: ATK & LUCK", new Color(100, 30, 150), new Color(30, 10, 45)),
    OPERATOR("Operator", "Scales with: ATK & SPD", new Color(160, 20, 30), new Color(40, 10, 15));
    
    public final String title, scaleDesc; 
    public final Color color, darkBg;
    
    ClassType(String t, String desc, Color c, Color bg) { 
        title = t; scaleDesc = desc; color = c; darkBg = bg; 
    }
}
