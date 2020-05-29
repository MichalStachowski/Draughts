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
            pygame.draw.circle(screen, (255, 255, 255), (self.y * self.sq_len + (self.sq_len // 2),
                                                         self.x * self.sq_len + (self.sq_len // 2)), self.radius)

    def draw_possible_moves(self, fields, screen):
        """
        If possible move - draw green circle. Otherwise draw red circle
        :param fields: List of instances of the field class. The most important parameter from here is "is_blank"
        :param screen: screen definied in main
        """
        fields_xy = [[field.x, field.y] for field in fields]

        if self.color == "black":
            # ..... piece .....
            # idx_l ..... idx_r
            try:
                idx_left = fields_xy.index([self.x + 1, self.y - 1])
            except ValueError:  # Boundary conditions
                idx_left = None

            try:
                idx_right = fields_xy.index([self.x + 1, self.y + 1])
            except ValueError:  # Boundary conditions
                idx_right = None
        else:
            # idx_l ..... idx_r
            # ..... piece .....
            try:
                idx_left = fields_xy.index([self.x - 1, self.y - 1])
            except ValueError:  # Boundary conditions
                idx_left = None

            try:
                idx_right = fields_xy.index([self.x - 1, self.y + 1])
            except ValueError:  # Boundary conditions
                idx_right = None

        if idx_left is not None:  # not draw if not possible
            if fields[idx_left].is_blank:
                self.draw_red_green_circle(screen, (0, 255, 0), fields[idx_left])  # green
            elif not fields[idx_left].is_blank:
                self.draw_red_green_circle(screen, (255, 0, 0), fields[idx_left])  # red

        if idx_right is not None:
            if fields[idx_right].is_blank:
                self.draw_red_green_circle(screen, (0, 255, 0), fields[idx_right])  # green
            elif not fields[idx_right].is_blank:
                self.draw_red_green_circle(screen, (255, 0, 0), fields[idx_right])  # red

    def draw_red_green_circle(self, screen, color, field):
        """
        Used in draw_possible_moves
        :param screen: screen definied in main
        :param color: Color which should be draw - red or green
        :param field: instance of Field class. Passed from "draw_possible_moves" as "fields[idx_right]"
        :return:
        """
        pygame.draw.circle(screen, color, (field.y * field.sq_len + (field.sq_len // 2),
                                                 field.x * field.sq_len + (field.sq_len // 2)), self.radius // 3)


