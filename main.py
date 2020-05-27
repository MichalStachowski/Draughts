import pygame
from board import Board

pygame.init()
screen = pygame.display.set_mode((400, 400))
b = Board(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    b.draw_board()
    pygame.display.update()
