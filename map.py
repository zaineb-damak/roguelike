
import pygame
import random
from monster import Goblin, Demon
from player import Player
from entity import Entity
from camera import Camera
import math


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 5
MAX_ROOMS = 30
MAX_ROOMS_MONSTERS = 3

class Tile(Entity):
    def __init__(self, blocks,tile_size,x,y):
        super().__init__('Tile', x, y, blocks)
        if blocks:
            self.name = 'wall'
        else : 
            self.name = 'floor'
               
        self.blocks = blocks        
        self.tile_size = tile_size
        self.image = pygame.image.load(f"./assets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.tile_size
        self.rect.y = y * self.tile_size
        self.rect.topleft = (self.rect.x, self.rect.y)

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
    def __init__(self, w, h, window, tile_size):
        self.width = w 
        self.height = h
        self.window = window
        self.tile_size = tile_size
        self.map=[[ Tile(True, self.tile_size, x, y) for y in range(self.height)] for x in range(self.width)]
        self.rooms = []
        self.wall_list = []
        self.monsters = []
        self.entities = []
        self.make_map()
        
        
        


    def distance(self, wall1, wall2):
        dist_x = wall2.rect.x - wall1.rect.x
        dist_y = wall2.rect.y - wall1.rect.y
        return math.hypot(dist_x*self.tile_size, dist_y*self.tile_size)

    def make_map(self):
        num_rooms = 0

        for _ in range(MAX_ROOMS):
            w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)

            
            x = random.randint(0, self.width - w  - 1)
            y = random.randint(0, self.height - h - 1)


            new_room = Room(x, y, w, h)
            failed = False
    
            for other_room in self.rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break
                
            if not failed:
                self.create_room(new_room)
                if num_rooms > 0:
                    prev_room = self.rooms[num_rooms - 1]
                    self.connect_rooms(prev_room, new_room)
               
                    
                #append the new room to the list
                self.place_monsters(new_room)
                self.rooms.append(new_room)
                num_rooms += 1

    
    def create_room(self,room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1,room.y2):
                self.map[x][y].blocks = False
            

    def connect_rooms(self, room1, room2):
        x1, y1 = room1.center()
        x2, y2 = room2.center()

        # Draw a horizontal tunnel first
        self.create_horizontal_tunnel(x1, x2, y1)
        # Then draw a vertical tunnel
        self.create_vertical_tunnel(y1, y2, x2)

    def create_horizontal_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y].blocks = False
            

    def create_vertical_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y].blocks = False
            
    
    def get_initial_room(self):
        if self.rooms:
            return self.rooms[0]
        else:
            return None

    def get_blocking_entity(self,x, y):
        ''' returns entity if it blocks else return none'''       
        #check for any blocking objects
        for entity in self.entities :
            if entity.blocks and entity.rect.x == x and entity.rect.y == y:
                return entity
        return None
        
    def place_monsters(self, room): 
        num_monsters = random.randint(1,MAX_ROOMS_MONSTERS)
        for i in range(num_monsters):
            x = random.randint(room.x1,room.x2) 
            y = random.randint(room.y1,room.y2)
            random_number = random.random() 
            if not self.map[x][y].blocks and self.get_blocking_entity(x,y) is None:
                if random_number<0.6:
                    monster = Goblin(x, y ,self,self.tile_size,True)
                else:
                    monster = Demon(x, y ,self,self.tile_size,True)
                
                self.monsters.append(monster)
            
    def get_pos(self, entity):
        return self.map[entity.x // self.tile_size][entity.y // self.tile_size]
    

     
    def draw_map(self):        
        for y in range(self.height):
            for x in range(self.width):
                wall = self.map[x][y]
                if wall.blocks:
                    self.window.blit(wall.image, (wall.rect.x, wall.rect.y))
                    self.wall_list.append(wall.rect)
                else:
                    pygame.draw.rect(self.window, BLACK, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
        
            
