import pygame

from .text import Text

pygame.font.init()


class Button:
    color = "black"

    def __init__(
        self,
        pos,
        size,
        color=color,
        hover_color=color,
        text=None,
        text_color="white",
        font="helvetica",
        font_size=None,
        font_color=None,
        func=None,
    ):
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size = font_size if font_size else int(self.size[1] * 0.7)
        self.font_color = font_color
        self.func = func

        if text:
            self.text_surface = Text(
                (self.size[0] / 2 + self.pos[0], self.size[1] / 2 + self.pos[1]),
                self.text,
                self.font_size,
                color=self.font_color,
                font=self.font,
            )

        self.crnt_color = color
        self.surface = pygame.Rect(*self.pos, *self.size)

    def draw(self, win):
        pygame.draw.rect(win, self.crnt_color, self.surface)
        self.text_surface.draw(win)

    def is_over(self, mpos):
        if self.surface.collidepoint(*mpos):
            self.crnt_color = self.hover_color
            return True
        self.crnt_color = self.color
        return False

    def call_back(self, *args, **kwargs):
        if self.func:
            self.func(*args, **kwargs)
