import pygame
from entity import Entity
from equipment import Equipment
import math
from camera import Camera

class Creature(Entity):
    def __init__(self, name, x, y,map, blocks, max_hp = 50, strength = 2, defense = 0):
        super().__init__(name,x,y, blocks)
        
        self.map = map
        self.wall_map = self.map.map
        self.tile_size = self.map.tile_size
        self.image = pygame.image.load(f"./assets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (18, 18))
        self.rect = self.image.get_rect()
        self.max_hp = max_hp
        self.hp = max_hp
        self.defense = defense
        self.strength = strength
        self.speed = 1 
        self.moves = True
        self.attack_cooldown = 0
        
   
    # @propert
    # def x(self):
    #     return self.x

    # @x.setter
    # def x(self, value):
    #     self.x = value
    #     # Update self.rect.x whenever self.x changes
    #     self.rect.x = value

    def distance(self,other):
        dist_x = other.rect.x - self.rect.x
        dist_y = other.rect.y - self.rect.y
        return math.hypot(dist_x, dist_y)

    
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
            if self.wall_map[corner_tile_x][corner_tile_y].blocks:
                return True  # Collision detected with a wall
    
        return False  # No collision detected

    def entities_collide(self, other):
        if self.rect.colliderect(other.rect):
            if isinstance(other,Creature):
                self.moves = False
                return True
            if isinstance(other,Equipment):
                return True
        else:
            self.moves = True
            return False
       
      
        
    def take_damage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.hp -= damage
        
   

               