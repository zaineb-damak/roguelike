# player.py

import pygame
from entity import Entity

class Player(Entity):
    def __init__(self,x, y, map,tile_size):
        super().__init__('player',x, y, map, tile_size)
        
        self.rect.topleft = self.set_initial_pos()

    def set_initial_pos(self):
        room = self.map.get_initial_room()
        (x,y) = room.center()
        return (x * self.tile_size, y*self.tile_size)
    
    def move(self):
        # Calculate the next position of the player
        keys_pressed = pygame.key.get_pressed()
        next_rect = self.rect.copy()
        if keys_pressed[pygame.K_LEFT]:
            next_rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            next_rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            next_rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            next_rect.y += self.speed

        # Check for collision with walls
        if not self.check_collision(next_rect):
            self.rect = next_rect
    