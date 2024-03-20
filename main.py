# main.py

import pygame
import sys
from player import Player
from map import Map
from monster import Monster
from item import Item
from engine import Engine

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rogue-like Game")

# Define colors


def main():
    # Create map and player
    game_map = Map()
    player = Player(400, 300, game_map.tiles)  # Pass the wall map data to the player
    monster = Monster(300, 300)

    # Create groups for monsters and items
    all_sprites = pygame.sprite.Group()
    monsters = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # Add player to all_sprites group
    all_sprites.add(player)
    all_sprites.add(monster)
    monsters.add(monster)

    engine = Engine(all_sprites, game_map, window, player)

    running = True

    while running:
        # Handle events
        engine.handle_events(events=pygame.event.get())
    
        # Handle player movement and render sprites
        engine.render()
        
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
