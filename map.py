# map.py

import pygame

class Map:
    def __init__(self):
        self.width = 20  # Number of tiles in the x direction
        self.height = 15  # Number of tiles in the y direction
        self.tile_size = 32  # Size of each tile in pixels

        # Example map data (2D list of integers representing tile types)
        self.tiles = [
            [1 if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1 else 0 for x in range(self.width)]
            for y in range(self.height)
        ]

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x]
                color = (255, 255, 255) if tile_type == 1 else (0, 0, 0)  # White for walls, black for empty space
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(surface, color, rect)
