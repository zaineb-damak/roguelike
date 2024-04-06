import pygame

WHITE = (255, 255, 255)

class Message:
    def __init__(self, text, color):
        self.text = text
        self.color = color
        self.count = 1
    
    @property
    def full_text(self):
        if self.count > 1:
            return f"{self.text} (x{self.count})"

class MessageLog:
    def __init__(self):
        self.messages = []

    def add_message(self, text, color=WHITE):
            self.messages.append(Message(text,color))
            if len(self.messages) > 6:
                self.messages.pop(0)

    def render_messages(self, surface):
        font = pygame.font.Font(None, 20)
        height = 780  # Starting y position
        y_offset = height - 1
        for message in reversed(self.messages):
            text= font.render(message.text, True, message.color)
            text_rect = text.get_rect()
            text_rect.center = (surface.get_width() // 2, y_offset)
            surface.blit(text, text_rect)
            y_offset -= 30

            if y_offset <0:
                return