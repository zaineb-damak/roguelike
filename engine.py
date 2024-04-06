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
    
    def initialize(self):
        self.game_map = Map(WIDTH // tile_size, HEIGHT//tile_size, self.window, tile_size)
        self.player =Player(400,300,self.game_map,blocks=True)
        self.monsters = self.game_map.monsters
        self.running = True
    
    def handle_events(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            
    def render_game_over_screen(self):
        # Clear the screen
        self.window.fill(BLACK)

        # Render game over message
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.window.blit(game_over_text, game_over_rect)

        # Render restart button
        button_text = font.render("Restart", True, WHITE)
        button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        pygame.draw.rect(self.window, (50, 50, 50), button_rect)  # Draw button background
        self.window.blit(button_text, button_rect)

        

        # Wait for the player to click the restart button
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_rect.collidepoint(mouse_pos):
                            self.initialize()
                            self.main()
            # Update the display
            pygame.display.flip()

    def render(self):
       
        #update player's moves
        self.player.update()
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
        self.initialize()
        self.window.fill(BLACK)
        pygame.display.flip()
        clock = pygame.time.Clock()  # Create a clock object
        FPS = 50  # Set desired FPS value
        # Create groups for monsters and items
        all_sprites = pygame.sprite.Group()
        items = pygame.sprite.Group()

        # Add player to all_sprites group
        all_sprites.add(self.player)
        all_sprites.add(self.game_map.monsters)
        self.game_map.entities = all_sprites
        self.game_map.player = self.player
        

        while self.running:
            # Handle events
            self.handle_events(pygame.event.get())

            clock.tick(FPS)
            # Handle player movement and render sprites
            self.render()  

            if self.player.dead:
            # If the player is dead, render the game over screen
                self.render_game_over_screen()
                    

        pygame.quit()
        sys.exit()
