import pygame
import random
import math
from creature import Creature

class Monster(Creature):
    def __init__(self, x, y,map, tile_size,blocks):
        super().__init__('demon',x, y, map, tile_size,blocks)
        self.rect.topleft = (x*self.tile_size, y*self.tile_size)  # Starting position of the monster
        self.image = pygame.transform.scale(self.image, (10, 10))

    def update(self):
        pass  # Add monster movement and other logic here

    # def set_initial_pos(self,room):
    #     x = random.randint(room.x1+1,room.x2-1) 
    #     y = random.randint(room.y1-1,room.y2+1) 
    #     if not self.map.map[x][y].blocked:
    #         self.x = x
    #         self.y = y
    #         self.rect.topleft = (self.x*self.tile_size, self.y*self.tile_size)
    #         print(self.rect.topleft)

    
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def move_to(self,player):
        # next_rect = self.rect.copy()
        # dist_x = dest_x - self.x
        # dist_y = dest_y - self.y
        # dist_x = dist_x // self.tile_size
        # dist_y = dist_y // self.tile_size
        # distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
        # print(distance)
        # dx = round(dist_x / distance)
        # dy = round(dist_y / distance)
        # # self.move(dx, dy)
        # if distance != 42:
        #     print("distance 2", distance)
        #     next_rect.x +=  dx
        #     next_rect.y +=  dy
        #     if not self.check_collision(next_rect):
        #         self.rect.x = next_rect.x 
        #         self.rect.y = next_rect.y 

        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.

            self.rect.x += dx 
            self.rect.y += dy 



    def attack(self,player):
        dist_x = player.rect.x - self.rect.x
        dist_y = player.rect.y - self.rect.y
        distance = math.hypot(dist_x, dist_y)
        print(distance)
        if distance <= 20:
            print("player is close")
            print(distance)
            self.move_to(player)
        elif player.hp > 0 and self.rect.colliderect(player.rect):
            print ("monster attacking")
            print(distance)
            player.hp -= 1
        elif player.hp <= 0 and self.rect.colliderect(player.rect):
            print ("player is dead")

        
