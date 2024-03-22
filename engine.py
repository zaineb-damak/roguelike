import pygame

class Engine:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    def __init__(self, entities, game_map, window,player):
        self.entities = entities
        self.game_map = game_map
        self.window = window
        self.player = player
        
    
    def handle_events(self,events):
         for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def render(self):
        #update player's moves
        self.player.update()

        # Clear the screen
        self.window.fill(self.BLACK)

        # Draw the map
        self.game_map.draw_map(self.window)

        # Draw all sprites (player, monsters, items)
        self.entities.draw(self.window)

        # Update the display
        pygame.display.flip()