package vanguards.core;

public class GameState {
    // Use Object for player to avoid cross-package dependency on nested Player class
    public Object player;
    public int encounters = 1;
}
