import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Map:
    def __init__(self, width, height, min_room_size, max_room_size):
        self.width = width
        self.height = height
        self.min_room_size = min_room_size
        self.max_room_size = max_room_size
        self.dungeon_map = [[1 for _ in range(width)] for _ in range(height)]  # Initialize map with walls

    def generate(self):
        self.split_recursive(0, 0, self.width, self.height)

    def split_recursive(self, x, y, w, h):
        # Split dungeon recursively until room size is reached
        if w < self.max_room_size * 2 or h < self.max_room_size * 2:
            return

        if random.random() < 0.5:  # Split horizontally
            split_pos = random.randint(y + self.min_room_size, y + h - self.min_room_size)
            for i in range(x, x + w):
                self.dungeon_map[split_pos][i] = 0  # Set tiles to empty space

            self.split_recursive(x, y, w, split_pos - y)
            self.split_recursive(x, split_pos, w, h - (split_pos - y))
        else:  # Split vertically
            split_pos = random.randint(x + self.min_room_size, x + w - self.min_room_size)
            for i in range(y, y + h):
                self.dungeon_map[i][split_pos] = 0  # Set tiles to empty space

            self.split_recursive(x, y, split_pos - x, h)
            self.split_recursive(split_pos, y, w - (split_pos - x), h)

    def draw_map(self, window):
        TILE_SIZE = min(window.get_width() // self.width, window.get_height() // self.height)

        # Draw map
        for y in range(self.height):
            for x in range(self.width):
                tile_color = WHITE if self.dungeon_map[y][x] == 0 else BLACK
                pygame.draw.rect(window, tile_color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))