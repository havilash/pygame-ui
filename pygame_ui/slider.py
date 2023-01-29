import pygame


class Slider:
    def __init__(self, pos, size, vrange=(0, 1), value=0):
        self.vrange = vrange
        self.rect = pygame.Rect(*pos, *size)
        self.value = value if vrange[0] < value < vrange[1] else 0
        self.circle_x, _ = pos + size[0] / vrange[1] * self.value
        self.circle_y = self.rect.h / 2 + self.rect.y
        self.circle_radius = self.rect.h * 1.5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.circle(
            screen,
            (255, 240, 255),
            (self.circle_x, self.circle_y),
            self.circle_radius,
        )

    def get_value(self):
        return self.value

    def set_value(self, num):
        self.value = num

    def update_value(self, x):
        if x < self.rect.x:
            self.value = self.vrange[0]
        elif x > self.rect.x + self.rect.w:
            self.value = self.vrange[1]
        else:
            self.value = (x - self.rect.x) / float(self.rect.w) * self.vrange[
                1
            ] + self.vrange[0]

    def is_over(self, pos):
        return self.rect.collidepoint(*pos) or (
            self.circle_x - self.circle_radius
            <= pos[0]
            <= self.circle_x + self.circle_radius
            and self.circle_y - self.circle_radius
            <= pos[1]
            <= self.circle_y + self.circle_radius
        )

    def update(self, x):
        if x < self.rect.x:
            self.circle_x = self.rect.x
        elif x > self.rect.x + self.rect.w:
            self.circle_x = self.rect.x + self.rect.w
        else:
            self.circle_x = x
        self.update_value(x)
