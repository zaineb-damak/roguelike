import pygame
from entity import Entity

class Equipment(Entity):
    def __init__(self, name, x, y,tile_size, blocks=True):
        super().__init__(name, x, y, blocks)
        self.image = pygame.image.load(f"./assets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*tile_size, y*tile_size)

    def move_to(self, other):
        pass

class Potion(Equipment):
    def __init__(self,tile_size, name='potion', x=0, y=0):
        super().__init__(name, x, y, tile_size)

class Coin(Equipment):
    def __init__(self,tile_size, name='coin', x=0, y=0):
        super().__init__(name, x, y, tile_size)
        self.image = pygame.transform.scale(self.image, (15, 15))