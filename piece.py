import pygame


class Piece:
    def __init__(self, x, y, radius, color, sq_len):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.sq_len = sq_len

    def draw(self, screen):
        if self.color == "black":
            pygame.draw.circle(screen, (0, 0, 0), (self.y*self.sq_len + (self.sq_len//2),
                                                   self.x*self.sq_len + (self.sq_len//2)), self.radius)
        else:
            pass
            pygame.draw.circle(screen, (255, 255, 255), (self.y * self.sq_len + (self.sq_len // 2),
                                                         self.x * self.sq_len + (self.sq_len // 2)), self.radius)
