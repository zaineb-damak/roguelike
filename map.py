
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 5
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
    def __init__(self, w, h, window, tile_size, player):
        self.collision_map=[[ Tile(True) for y in range(h)] for x in range(w)]
        self.width = w - (tile_size * 2)
        self.height = h- (tile_size * 2)
        self.window = window
        self.tile_size = tile_size
        self.player = player
        self.map=[[ Tile(True) for y in range(self.height)] for x in range(self.width)]
        self.make_map()

    def make_map(self):
        rooms = []
        num_rooms = 0

        for r in range(MAX_ROOMS):
            w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)

            
            x = random.randint(0, self.width - w  - 1)
            y = random.randint(0, self.height - h - 1)


            new_room = Room(x, y, w, h)
            failed = False
    
            for other_room in rooms:
                if new_room.intersect(other_room):
                    failed = True
                    print("failed true")
                    break
                
            if not failed:
                self.create_room(new_room)
                if num_rooms > 0:
                    prev_room = rooms[num_rooms - 1]
                    if not self.is_connected(prev_room, new_room):
                        self.connect_rooms(prev_room, new_room)
                
                #append the new room to the list
                rooms.append(new_room)
                num_rooms += 1
                print(num_rooms)
                


    
    def create_room(self,room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1,room.y2):
                self.map[x][y].blocked = False
                self.map[x][y].block_sight = False
    
    def is_connected(self, room1, room2):
        center1 = room1.center()
        center2 = room2.center()

        x1, y1 = center1
        x2, y2 = center2

        # Check if there is already a tunnel between the rooms
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if not self.map[x1][y].blocked:
                    return True
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if not self.map[x][y1].blocked:
                    return True
        
        return False

    def connect_rooms(self, room1, room2):
        center1 = room1.center()
        center2 = room2.center()

        x1, y1 = center1
        x2, y2 = center2

        # Draw a horizontal tunnel first
        self.create_horizontal_tunnel(min(x1, x2), max(x1, x2), y1)

        # Then draw a vertical tunnel
        self.create_vertical_tunnel(y1, y2, x2)

    def create_horizontal_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False

    def create_vertical_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False
                
    def draw_map(self ):
        for y in range(self.height + self.tile_size*2):
            for x in range(self.width + self.tile_size*2):
                wall = self.collision_map[x][y].blocked
                if wall:
                    color = WHITE
                else:
                    color = BLACK
                
                pygame.draw.rect(self.window, color, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
        
        for y in range(self.height):
            for x in range(self.width):
                wall = self.map[x][y].blocked
                if wall:
                    color = WHITE
                else:
                    color = BLACK
                
                pygame.draw.rect(self.window, color, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

