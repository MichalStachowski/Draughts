from field import Field
from piece import Piece


class Board:
    def __init__(self, screen):
        self.fields = []
        self.pieces = []
        self.screen = screen
        self.init_fields()
        self.init_pieces()

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

    def init_pieces(self):
        for i in range(3):
            if i == 1:
                for j in range(0, 7, 2):
                    piece = Piece(i, j, radius=20, color="black", sq_len=50)
                    self.pieces.append(piece)
            else:
                for j in range(1, 8, 2):
                    piece = Piece(i, j, radius=20, color="black", sq_len=50)
                    self.pieces.append(piece)

        for i in range(5, 8):
            if i == 6:
                for j in range(1, 8, 2):
                    piece = Piece(i, j, radius=20, color="white", sq_len=50)
                    self.pieces.append(piece)
            else:
                for j in range(0, 7, 2):
                    piece = Piece(i, j, radius=20, color="white", sq_len=50)
                    self.pieces.append(piece)

    def draw_board(self):
        for field in self.fields:
            field.draw(self.screen)

        for piece in self.pieces:
            piece.draw(self.screen)

    def print_param(self):
        for field in self.fields:
            print(field.x, field.y, field.color, field.sq_len)
