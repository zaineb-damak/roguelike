import pygame
import sys
from player import Player
from map import Map
from monster import Monster
from item import Item
from camera import Camera
from message_log import MessageLog




# Set up the display

tile_size = 25
WIDTH, HEIGHT = 1000, 800
pygame.display.set_caption("Rogue-like Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Engine:
   
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
    
    def add_sprites(self):
        all_sprites = pygame.sprite.Group()
        player = pygame.sprite.Group()

        # Add player to all_sprites group
        all_sprites.add(self.game_map.monsters)
        all_sprites.add(self.game_map.equipments)
        all_sprites.add(self.game_map.stairs)
        player.add(self.player)
        self.game_map.entities = all_sprites
        self.game_map.player = player
   
    def initialize(self):
        self.message_log = MessageLog()
        self.game_map = Map(800 // tile_size, 600//tile_size, self.window, tile_size, self.message_log)
        self.player =Player(400,300,self.game_map,blocks=True)
        self.monsters = self.game_map.monsters
        self.running = True

        self.add_sprites()

        
    
    def create_new_level(self):
        if len(self.game_map.monsters) == 0:
            self.game_map = Map(800 // tile_size, 600//tile_size, self.window, tile_size, self.message_log)
            self.monsters = self.game_map.monsters
            self.add_sprites()
    
    def handle_events(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.player.use_item(0)
                elif event.key == pygame.K_2:
                    self.player.use_item(1)
                elif event.key == pygame.K_3:
                    self.player.use_item(2)
                elif event.key == pygame.K_4:
                    self.player.use_item(3)
                elif event.key == pygame.K_5:
                    self.player.use_item(4)
            
    def render_player_status(self):
        font = pygame.font.Font(None, 20)
        x = 900
        y_offset = 100
        
        status_attributes = [
            ("Player's hp", self.player.hp),
            ("Player's strength", self.player.strength),
            ("Player's defense", self.player.defense),
            ("Player's XP", self.player.xp),
            ("Player's level", self.player.level),
            ("Player's coins", self.player.coin),
        ]
        
        for attribute_name, attribute_value in status_attributes:
            text_surface = font.render(attribute_name, True, WHITE)
            text_rect = text_surface.get_rect(center=(x, y_offset))
            self.window.blit(text_surface, text_rect)
            
            value_surface = font.render(str(attribute_value), True, WHITE)
            value_rect = value_surface.get_rect(center=(x, y_offset + 20))
            self.window.blit(value_surface, value_rect)
            
            y_offset += 50
        
      
        inventory_attributes = []
        inventory_attributes.append(("Player's inventory", ""))
        inventory_attributes.append(("item 1", ""))
        inventory_attributes.append(("item 2",""))
        inventory_attributes.append(("item 3", ""))
        inventory_attributes.append(("item 4", ""))
        inventory_attributes.append(("item 5", ""))
        

        for i in range(self.player.inventory_size):
            if len(self.player.inventory) > i:
                inventory_attributes[i+1]= ("item " + str(i + 1), self.player.inventory[i].name)

        for name, value in inventory_attributes:
            text_surface = font.render(name, True, WHITE)
            text_rect = text_surface.get_rect(center=(x, y_offset))
            self.window.blit(text_surface, text_rect)
            
            value_surface = font.render(value, True, WHITE)
            value_rect = value_surface.get_rect(center=(x, y_offset + 20))
            self.window.blit(value_surface, value_rect)
            
            y_offset += 50
    
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
        for entity in self.game_map.entities:
            entity.move_to(self.player)
            if self.player.entities_collide(entity):
                self.player.meet(entity)
        
        # Clear the screen
        self.window.fill(BLACK)
         
        # Display messages
        self.message_log.render_messages(self.window)
        self.render_player_status()
        

        # Draw the map
        self.create_new_level()
        self.game_map.draw_map()

        # Draw all sprites (player, monsters, items)
        self.game_map.player.draw(self.window)
        self.game_map.entities.draw(self.window)
       
        
        # Update the display
        pygame.display.flip()

    

    def main(self):
        # Initialize Pygame
        pygame.init()
        self.initialize()
      
        clock = pygame.time.Clock()  # Create a clock object
        FPS = 50  # Set desired FPS value
        # Create groups for monsters and items
        
              

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
