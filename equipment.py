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

class Weapon(Equipment):
    def __init__(self,tile_size, name='weapon', x=0, y=0):
        super().__init__(name, x, y, tile_size)
        self.usage_count = 0
        self.max_usage_count = 5
        self.extra_strength = 2

class Armor(Equipment):
    def __init__(self,tile_size, name='armor', x=0, y=0):
        super().__init__(name, x, y, tile_size)
        self.usage_count = 0
        self.max_usage_count = 5
        self.extra_defense = 2