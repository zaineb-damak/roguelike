# player.py

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((32, 32))  # Placeholder image for now
        self.image.fill((255, 0, 0))  # Red rectangle representing the player
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Starting position of the player
        self.speed = 5  # Adjust the movement speed here
    
    def update(self):
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

        # Check for collision with walls
        # if not self.check_collision(next_rect):
        self.rect = next_rect

    def check_collision(self, rect):
        # Check if the next position collides with any walls
        for row in range(len(self.wall_map)):
            for col in range(len(self.wall_map[row])):
                if self.wall_map[row][col] == 1:
                    wall_rect = pygame.Rect(col * 32, row * 32, 32, 32)
                    if rect.colliderect(wall_rect):
                        return True
        return False
