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
global tile_size
tile_size = 10
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rogue-like Game")


def main():
    # Create map and player
    
    game_map = Map(80, 60, window, tile_size)
    player = Player(400,300,game_map, tile_size) 
    
    #monster = Monster(300, 300)
 
    # Create groups for monsters and items
    all_sprites = pygame.sprite.Group()
    monsters = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # Add player to all_sprites group
    all_sprites.add(player)
    all_sprites.add(game_map.monsters)
    monsters.add(monsters)

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
