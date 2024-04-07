import pygame

class Entity(pygame.sprite.Sprite): 
    def __init__(self, name, x, y, blocks=False):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.blocks = blocks

    def move_to(self,other):
        pass
       
    
    
   

   
            
