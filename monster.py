import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/demon.png")  # Placeholder image for now
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Starting position of the monster

    def update(self):
        pass  # Add monster movement and other logic here
