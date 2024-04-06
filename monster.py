import pygame
import random
import math
from creature import Creature
from equipment import Equipment
import time

class Monster(Creature):
    def __init__(self,name, x, y,map, tile_size,blocks):
        super().__init__(name,x, y, map, tile_size,blocks)
        self.rect.topleft = (x*self.tile_size, y*self.tile_size)  # Starting position of the monster
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.turn = True

    
    def move_to(self,player):
        next_rect = self.rect.copy()
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        distance = math.hypot(dx, dy)
        if distance <= 50 and distance>1:
            dx, dy = dx / distance, dy / distance  # Normalize.
           

            next_rect.x += dx * self.speed
            next_rect.y += dy * self.speed

        # Move along this normalized vector towards the player at current speed.
            if not self.check_collision(next_rect) and not self.rect.colliderect(player.rect) :
            
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed

 
    
    def attack(self,player):
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        damage = self.strength - player.defense
        if player.hp > 0 and self.rect.colliderect(player.rect) and self.turn and self.attack_cooldown == 0:
            print (f"{self.name} attacks {player.name} for {damage} hit points")
            player.take_damage(damage)
            print("player hp", player.hp)
            self.attack_cooldown = 20
            self.turn = False

        elif player.hp <= 0:
            print ("player is dead")
            player.dead = True
           
    def dies(self):
        if self.hp <= 0:
            self.moves = False 
            self.map.monsters.remove(self)
            self.map.entities.remove(self)

        
class Demon(Monster):
    def __init__(self,x, y, map, tile_size, blocks, hp=25, strength =5):
        super().__init__('demon',x,y, map,tile_size, blocks)
        self.hp = hp
        self.strength = strength
        self.added_xp = 2

class Goblin(Monster):
    def __init__(self, x, y, map, tile_size, blocks, hp=15, strength =3):
        super().__init__('goblin',x,y, map,tile_size, blocks)
        self.hp = hp
        self.strength = strength
        self.added_xp = 1