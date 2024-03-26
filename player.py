# player.py

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x, y, map,tile_size):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 1  
        self.map = map
        self.wall_map = self.map.map
        self.tile_size = tile_size
        self.image = pygame.image.load("./assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.set_initial_pos()

    def set_initial_pos(self):
        room = self.map.get_initial_room()
        (x,y) = room.center()
        return (x * self.tile_size, y*self.tile_size)
    
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
        if not self.check_collision(next_rect):
            self.rect = next_rect

    def check_collision(self, next_rect):
        # # Calculate the grid position of the next tile's top-left corner
        # tile_x = next_x // self.tile_size
        # tile_y = next_y // self.tile_size

        # # Check if any corner of the player's bounding box collides with a wall
        # corners = [(next_x, next_y),                                    # Top-left
        #            (next_x + self.rect.width, next_y),                   # Top-right
        #            (next_x, next_y + self.rect.height),                  # Bottom-left
        #            (next_x + self.rect.width, next_y + self.rect.height) # Bottom-right
        #           ]

        # for corner in corners:
        #     # Calculate the grid position of the corner
        #     corner_tile_x = corner[0] // self.tile_size
        #     corner_tile_y = corner[1] // self.tile_size

        #     # Check if the corner is within the boundaries of the map
        #     if (0 <= corner_tile_x < len(self.wall_map[0])) and (0 <= corner_tile_y < len(self.wall_map)):
        #         # Check if the corner corresponds to a wall
        #         if self.wall_map[corner_tile_y][corner_tile_x].blocked:
        #             return True  # Collision detected with a wall
        
        # return False  # No collision detected
        # Check if the next position collides with any wall rectangle
        for wall_rect in self.map.wall_list:
            if next_rect.colliderect(wall_rect):
                print("true")
                print(next_rect)
                print(wall_rect)
                return True
        return False
