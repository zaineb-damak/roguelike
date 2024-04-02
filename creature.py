import pygame
from entity import Entity
import math

class Creature(Entity):
    def __init__(self, name, x, y,map, blocks, hp = 5, defense = 5, xp = 5):
        super().__init__(name,x,y, blocks)
        
        self.map = map
        self.wall_map = self.map.map
        self.tile_size = self.map.tile_size
        self.image = pygame.image.load(f"./assets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect()
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.xp = xp
        self.speed = 1 
       
    # @property
    # def x(self):
    #     return self.x

    # @x.setter
    # def x(self, value):
    #     self.x = value
    #     # Update self.rect.x whenever self.x changes
    #     self.rect.x = value

    #def distance(self,other):
        # dx = dest_x - self.x
        # dy = dest_y - self.y
        # return math.sqrt(dx ** 2 + dy ** 2)
       
        # x = other.x - self.x
        # y = other.y - self.y
        # if x<0 and y>0:
        #     return self.wall_map[][]

    
    def check_collision(self, dest):
       
        #Check if any corner of the player's bounding box collides with a wall
        corners = [(dest.x, dest.y),                                    # Top-left
                   (dest.x + self.rect.width, dest.y),                   # Top-right
                   (dest.x, dest.y+ self.rect.height),                  # Bottom-left
                   (dest.x + self.rect.width, dest.y + self.rect.height) # Bottom-right
                  ]

        for corner in corners:
            # Calculate the grid position of the corner
            corner_tile_x = corner[0] // self.tile_size
            corner_tile_y = corner[1] // self.tile_size
            
            # Check if the corner corresponds to a wall
            if self.wall_map[corner_tile_x][corner_tile_y].blocked:
                return True  # Collision detected with a wall
    
        return False  # No collision detected
       
    
        

               