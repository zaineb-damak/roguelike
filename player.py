# player.py

import pygame
from creature import Creature
from monster import Monster
from equipment import Equipment

class Player(Creature):
    def __init__(self,x, y,map,blocks):
        super().__init__('player',x, y, map,blocks)
        self.rect.topleft = self.set_initial_pos()
        self.dead = False
        self.speed = 2
        self.turn = False
        self.attack_cooldown = 0

    def set_initial_pos(self):
        room = self.map.get_initial_room()
        (x,y) = room.center()
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
        if not self.check_collision(dest) and self.moves:
            self.rect = dest
       
        
        

    def meet(self, entity):
        if isinstance(entity, Monster):
            print("combat starting")
            self.attack(entity)
        if isinstance(entity, Equipment):
            pass
        else:
            return
         

    def attack(self, entity):
        entity.attack(self)
        # print("player ", self.attack_cooldown)
        # if self.attack_cooldown > 0:
        #     self.attack_cooldown -= 1
       
        damage = self.strength - entity.defense
        if damage > 0 and self.turn and self.attack_cooldown == 0 :
            print(f"{self.name} attacks {entity.name} for {damage} hit points")
            entity.take_damage(damage)
            #self.attack_cooldown = 60
            self.turn = False
            entity.turn = True
            
        elif damage<0 and self.attack_cooldown == 0 and self.turn:
            print(f"{self.name} attacks {entity.name} but it has no effect")

        elif entity.hp <= 0:
            print ("monster is dead")
            entity.dies()
            #self.moves = True
        
