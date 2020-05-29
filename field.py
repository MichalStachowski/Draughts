import pygame


class Field:
    def __init__(self, x, y, sq_len, color):
        self.x = x
        self.y = y
        self.sq_len = sq_len
        self.color = color
        self.is_blank = True  # false if piece on field, otherwise true

    def draw(self, screen):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 10)

        if self.color == "light":
            pygame.draw.rect(screen, (255, 255, 102), (self.x * self.sq_len, self.y * self.sq_len,
                                                            self.sq_len, self.sq_len))
        else:
            pygame.draw.rect(screen, (102, 51, 0), (self.x * self.sq_len, self.y * self.sq_len,
                                                         self.sq_len, self.sq_len))

        textsurface = myfont.render(f"{self.x} {self.y}", False, (0, 0, 0))
        screen.blit(textsurface, (self.x * self.sq_len, self.y * self.sq_len))
