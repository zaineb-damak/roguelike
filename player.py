# player.py

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, map,tile_size):
        super().__init__()
        self.map = map
        self.tile_size = tile_size
        (self.x, self.y)= self.set_initial_pos()
        print(self.x, self.y)
        self.image = pygame.image.load("./assets/player.png")
        self.rect = self.image.get_rect()
        # Starting position of the player
        self.rect.topleft = (self.x*tile_size, self.y*tile_size)
        self.speed = 1  # Adjust the movement speed here
       
        #self.set_initial_pos()

    def set_initial_pos(self):
        room = self.map.get_initial_room()
        (x,y) = room.center()
        return (x,y)
    
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
