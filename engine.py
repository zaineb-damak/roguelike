import pygame
import sys
from player import Player
from map import Map
from monster import Monster
from item import Item




# Set up the display

tile_size = 10
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Rogue-like Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Engine:
   
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_map = Map(80, 60, self.window, tile_size)
        self.player =Player(400,300,self.game_map, tile_size, True)
        
    
    def handle_events(self,events):
         for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def render(self):
        #update player's moves
        self.player.move()

        # Clear the screen
        self.window.fill(BLACK)

        # Draw the map
        self.game_map.draw_map()

        # Draw all sprites (player, monsters, items)
        #self.game_map.entities.draw(self.window)
        

        # Update the display
        pygame.display.flip()

    def main(self):
        # Initialize Pygame
        pygame.init()
        # Create groups for monsters and items
        all_sprites = pygame.sprite.Group()
        monsters = pygame.sprite.Group()
        items = pygame.sprite.Group()

        # Add player to all_sprites group
        all_sprites.add(self.player)
        all_sprites.add(self.game_map.monsters)
        monsters.add(monsters)
        self.game_map.entities = all_sprites
        
        running = True

        while running:
            # Handle events
            self.handle_events(events=pygame.event.get())
        
            # Handle player movement and render sprites
            self.render()       

        pygame.quit()
        sys.exit()
