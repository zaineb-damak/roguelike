import pygame

class Camera:
    def __init__(self, offset_x=100, offset_y=200):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.offset = pygame.math.Vector2(10,20)

        self.display_surface = pygame.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
        