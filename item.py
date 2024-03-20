import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # Placeholder image for now
        self.image.fill((0, 0, 255))  # Blue rectangle representing the item
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Starting position of the item

    def update(self):
        pass  # Add item interaction logic here