# import pygame
# import random

# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BROWN = (139, 69, 19)  # Door color

# class Map:
#     def __init__(self, width, height, min_room_size, max_room_size):
#         self.width = width
#         self.height = height
#         self.min_room_size = min_room_size
#         self.max_room_size = max_room_size
#         self.map_data = [[0 for _ in range(width)] for _ in range(height)]  # Initialize map with empty space
#         self.generate()

#     def generate(self):
#         # Add walls around the border
#         for x in range(self.width):
#             self.map_data[0][x] = 1  # Top border
#             self.map_data[self.height - 1][x] = 1  # Bottom border
#         for y in range(self.height):
#             self.map_data[y][0] = 1  # Left border
#             self.map_data[y][self.width - 1] = 1  # Right border

#         # Split recursively to generate dungeon
#         self.split_recursive(1, 1, self.width - 2, self.height - 2)  # Start from (1, 1) to leave a border of walls

#     def split_recursive(self, x, y, w, h):
#         # Split dungeon recursively until room size is reached
#         if w < self.max_room_size * 2 or h < self.max_room_size * 2:
#             return

#         if random.random() < 0.5:  # Split horizontally
#             split_pos = random.randint(y + self.min_room_size, y + h - self.min_room_size)
#             door_x = random.randint(x + 1, x + w - 2)  # Random x position for door
#             self.map_data[split_pos][door_x] = 2  # Set tile to door
#             for i in range(x, x + w):
#                 self.map_data[split_pos][i] = 1  # Set tiles to wall

#             self.split_recursive(x, y, w, split_pos - y)
#             self.split_recursive(x, split_pos, w, h - (split_pos - y))
#         else:  # Split vertically
#             split_pos = random.randint(x + self.min_room_size, x + w - self.min_room_size)
#             door_y = random.randint(y + 1, y + h - 2)  # Random y position for door
#             self.map_data[door_y][split_pos] = 2  # Set tile to door
#             for i in range(y, y + h):
#                 self.map_data[i][split_pos] = 1  # Set tiles to wall

#             self.split_recursive(x, y, split_pos - x, h)
#             self.split_recursive(split_pos, y, w - (split_pos - x), h)

#     def draw_map(self, window):
#         TILE_SIZE = min(window.get_width() // self.width, window.get_height() // self.height)

#         # Draw map
#         for y in range(self.height):
#             for x in range(self.width):
#                 if self.map_data[y][x] == 1:
#                     tile_color = WHITE  # Wall color
#                 elif self.map_data[y][x] == 2:
#                     tile_color = BROWN  # Door color
#                 else:
#                     tile_color = BLACK  # Empty space color
#                 pygame.draw.rect(window, tile_color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked
       
        self.block_sight = block_sight

class Room:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + w
        self.y2 = self.y1 + h
   
    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return(center_x, center_y)
    
    def intersect(self, other):
        #returns true if a room intersects with another one
        return(self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1) 


    


class Map:
    def __init__(self, width, height, window, tile_size, player):
        self.width = width
        self.height = height
        self.window = window
        self.tile_size = tile_size
        self.player = player
        self.map=[]
        self.make_map()

    def make_map(self):
        self.map=[[ Tile(True) for y in range(self.height)] for x in range(self.width)]
        
        rooms = []
        num_rooms = 0

        for r in range(MAX_ROOMS):
            w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)

            x = random.randint(0, self.width - w - 1)
            y = random.randint(0, self.height - h - 1)

            new_room = Room(x, y, w, h)
            failed = False
            
            for other_room in rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break
            if not failed:
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    #this is the first room, where the player starts at
                    self.player.x = new_x
                    self.player.y = new_y
                else:
                    #all rooms after the first:
                    #connect it to the previous room with a tunnel

                    (prev_x, prev_y) = rooms[num_rooms-1].center()

                    if random.randint(0,1) == 1:
                        #first move horizontally then vertically
                        self.create_h_tunnel(prev_y, new_y,prev_x)
                        self.create_v_tunnel(prev_x, new_x, new_y)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x,prev_y)
            
                     #append the new room to the list
                    rooms.append(new_room)
                    num_rooms += 1
                


    
    def create_room(self,room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1,room.y2):
                self.map[x][y].blocked = False
                self.map[x][y].block_sight = False
    
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False
    
    def create_v_tunnel(self,y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False

    def draw_map(self ):
        for y in range(self.height):
            for x in range(self.width):
                wall = self.map[x][y].blocked
                if wall:
                    color = WHITE
                else:
                    color = BLACK
                
                pygame.draw.rect(self.window, color, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

