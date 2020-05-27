import pygame
from field import Field


class Board:
    def __init__(self, screen):
        self.fields = []
        self.screen = screen
        self.init_fields()

    def init_fields(self):
        for i in range(8):
            for j in range(0, 8, 2):
                if i % 2 == 0:
                    light_field = Field(i, j, 50, "light")
                    dark_field = Field(i, j+1, 50, "dark")
                else:
                    dark_field = Field(i, j, 50, "dark")
                    light_field = Field(i, j+1, 50, "light")

                self.fields.append(light_field)
                self.fields.append(dark_field)

        self.print_param()

    def draw_board(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 10)

        for field in self.fields:

            if field.color == "light":
                pygame.draw.rect(self.screen, (255, 255, 102), (field.x*field.sq_len, field.y*field.sq_len,
                                                                field.sq_len, field.sq_len))
            else:
                pygame.draw.rect(self.screen, (102, 51, 0), (field.x * field.sq_len, field.y * field.sq_len,
                                                                field.sq_len, field.sq_len))

            textsurface = myfont.render(f"{field.x} {field.y}", False, (0, 0, 0))
            self.screen.blit(textsurface, (field.x * field.sq_len, field.y * field.sq_len))

    def print_param(self):
        for field in self.fields:
            print(field.x, field.y, field.color, field.sq_len)
