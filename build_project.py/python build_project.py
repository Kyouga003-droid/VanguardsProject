import os
import sys

# 1. The Lock Mechanism
LOCK_FILE = ".setup_complete"

if os.path.exists(LOCK_FILE):
    print("❌ Setup aborted: The lock file '.setup_complete' exists.")
    print("If you really want to run this again, delete that file first.")
    sys.exit(0)

# 2. Define the Package Structure
BASE_DIR = "src/vanguards"
FOLDERS = {
    "enums": f"{BASE_DIR}/enums",
    "entities": f"{BASE_DIR}/entities",
    "items": f"{BASE_DIR}/items",
    "ui": f"{BASE_DIR}/ui",
    "core": f"{BASE_DIR}/core"
}

# 3. Create the Directories
print("📁 Creating package directories...")
for name, path in FOLDERS.items():
    os.makedirs(path, exist_ok=True)
    print(f"  -> Created {path}")

# 4. Define the Segregated File Contents
# Note: These are the cleanly decoupled data models. 
# Package declarations and imports have been added for you.
files_to_create = {
    f"{FOLDERS['enums']}/ClassType.java": """package vanguards.enums;

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
""",

    f"{FOLDERS['enums']}/Rarity.java": """package vanguards.enums;

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
""",

    f"{FOLDERS['items']}/Item.java": """package vanguards.items;

import vanguards.enums.Rarity;

public class Item {
    public String name;
    public int price; 
    public Rarity rarity;
    
    public Item(String n, int p, Rarity r) { 
        name = n; price = p; rarity = r; 
    }
}
""",

    f"{FOLDERS['core']}/GameState.java": """package vanguards.core;

import vanguards.entities.Player;

public class GameState { 
    public Player player; 
    public int encounters = 1; 
}
"""
}


print("\n📝 Generating Java files...")
for file_path, content in files_to_create.items():
    with open(file_path, "w") as f:
        f.write(content)
    print(f"  -> Wrote {file_path}")


ui_stubs = ["BattlePanel.java", "TitleScreen.java", "DeathScreen.java", "ClassSelect.java", "StylizedButton.java"]
for stub in ui_stubs:
    stub_path = f"{FOLDERS['ui']}/{stub}"
    with open(stub_path, "w") as f:
        class_name = stub.replace(".java", "")
        f.write(f"package vanguards.ui;\n\nimport javax.swing.*;\n\npublic class {class_name} extends JPanel {{\n    // TODO: Migrate logic from Vanguards.java\n}}\n")
    print(f"  -> Wrote UI Stub: {stub_path}")


with open(LOCK_FILE, "w") as f:
    f.write("Project segregated successfully. Delete this file to allow the script to run again.")

print("\n✅ Success! The project has been segregated. The setup is now locked.")