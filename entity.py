import pygame

class Entity(pygame.sprite.Sprite):
    
    def __init__(self, name, x, y,map, tile_size):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.speed = 1 
        self.map = map
        self.wall_map = self.map.map
        self.tile_size = tile_size
        self.image = pygame.image.load(f"./assets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
        self.hurt = False
        self.dead = False
        self.can_move = True
        self.time = 0
        self.can_get_hurt = True
    
   

    def check_collision(self, next_rect):
       

        #Check if any corner of the player's bounding box collides with a wall
        corners = [(next_rect.x, next_rect.y),                                    # Top-left
                   (next_rect.x + self.rect.width, next_rect.y),                   # Top-right
                   (next_rect.x, next_rect.y+ self.rect.height),                  # Bottom-left
                   (next_rect.x + self.rect.width, next_rect.y + self.rect.height) # Bottom-right
                  ]

        for corner in corners:
            # Calculate the grid position of the corner
            corner_tile_x = corner[0] // self.tile_size
            corner_tile_y = corner[1] // self.tile_size

            # Check if the corner is within the boundaries of the map
            if (0 <= corner_tile_x < len(self.wall_map[0])) and (0 <= corner_tile_y < len(self.wall_map)):
                # Check if the corner corresponds to a wall
                if self.wall_map[corner_tile_x][corner_tile_y].blocked:
                    return True  # Collision detected with a wall
        
        return False  # No collision detected
       
    
        

               
            
