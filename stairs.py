import pygame
from entity import Entity

class Stairs(Entity):
    def __init__(self, x, y,map, blocks=True):
        super().__init__('stairs', x, y, blocks)
        self.image = pygame.image.load(f"./assets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.set_initial_pos(map)

    def set_initial_pos(self, map):
        room = map.get_last_room()
        (x,y) = room.center()
        return (x * map.tile_size, y * map.tile_size)
    
    