import pygame
import sys
from player import Player
from map import Map
from monster import Monster
from item import Item
from camera import Camera




# Set up the display

tile_size = 25
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Rogue-like Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Engine:
   
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_map = Map(WIDTH // tile_size, HEIGHT//tile_size, self.window, tile_size)
        self.player =Player(400,300,self.game_map,blocks=True)
        self.monsters = self.game_map.monsters
        
    
    def handle_events(self,events):
         for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def render(self):
    
        #update player's moves
        self.player.move()
        for monster in self.monsters:
            monster.move_to(self.player)
            if self.player.entities_collide(monster):
                self.player.meet(monster)
        
        # Clear the screen
        self.window.fill(BLACK)

        # Draw the map
        self.game_map.draw_map()

        # Draw all sprites (player, monsters, items)
        self.game_map.entities.draw(self.window)
        

        # Update the display
        pygame.display.flip()

    def main(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()  # Create a clock object
        FPS = 50  # Set desired FPS value
        # Create groups for monsters and items
        all_sprites = pygame.sprite.Group()
        monsters = pygame.sprite.Group()
        items = pygame.sprite.Group()

        # Add player to all_sprites group
        all_sprites.add(self.player)
        all_sprites.add(self.game_map.monsters)
        monsters.add(monsters)
        self.game_map.entities = all_sprites
        self.game_map.player = self.player
        
        running = True

        while running:
            # Handle events
            self.handle_events(events=pygame.event.get())

            clock.tick(FPS)
            # Handle player movement and render sprites
            self.render()       

        pygame.quit()
        sys.exit()
