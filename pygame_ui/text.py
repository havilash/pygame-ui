import pygame

pygame.font.init()


class Text:
    color = "black"

    def __init__(self, center_pos, text, size=10, font="helvetica", color=color):
        self.center_pos = center_pos
        self.size = size
        self.text = text
        if font.endswith((".ttf", ".otf")):
            self.font = pygame.font.Font(font, self.size)
        elif type(font) == pygame.font.Font:
            self.font = font
        else:
            self.font = pygame.font.SysFont(font, self.size)
        self.color = color

    def draw(self, win):
        self.surface = self.font.render(self.text, False, self.color)
        self.font_size = self.surface.get_size()
        self.pos = (
            self.center_pos[0] - self.font_size[0] / 2,
            self.center_pos[1] - self.font_size[1] / 2,
        )
        self.x, self.y = self.pos

        win.blit(self.surface, self.pos)

    def set_text(self, text):
        self.text = text
