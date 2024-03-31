# player.py

import pygame
from creature import Creature

class Player(Creature):
    def __init__(self,x, y, map,tile_size,blocks):
        super().__init__('player',x, y, map,tile_size, blocks)
        self.rect.topleft = self.set_initial_pos()
        self.speed = 1 
        self.velocity = [0, 0]
        self.hurt = False
        self.dead = False
        self.can_move = True
        self.time = 0
        self.can_get_hurt = True
        self.is_attacking = False

    def set_initial_pos(self):
        room = self.map.get_initial_room()
        (x,y) = room.center()
        print(x*self.tile_size,y*self.tile_size)
        return (x * self.tile_size, y * self.tile_size)
    
    
    def input(self):
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
        return next_rect

    def move(self):
    # Check for collision with walls
        dest = self.input()
        if not self.check_collision(dest) and self.map.get_blocking_entity(dest.x // self.tile_size, dest.y//self.tile_size) is None:
            self.rect = dest
        elif self.map.get_blocking_entity(dest.x // self.tile_size, dest.y//self.tile_size):
            self.attack()

    def attack(self):
        target = self.map.get_blocking_entity(self.x, self.y)
        if not target:
            return
        print(f" attack {target.name}")
        self.is_attacking = True
