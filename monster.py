import pygame
import random
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

