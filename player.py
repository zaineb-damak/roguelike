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
    
    