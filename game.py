import pygame
import random
import math

pygame.init()

FPS = 60

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
NUMBER_OF_ROWS = 4
NUMBER_OF_COLUMNS = 4

RECT_HEIGHT = WINDOW_HEIGHT // NUMBER_OF_ROWS
RECT_WIDTH = WINDOW_WIDTH // NUMBER_OF_COLUMNS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLIR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VELOCITY = 20

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2048")        

class Tile:
    pass

def draw_grid(window):
    for row in range(1, NUMBER_OF_ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WINDOW_WIDTH, y), OUTLINE_THICKNESS)
    
    for column in range(1, NUMBER_OF_COLUMNS):
        x = column * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, WINDOW_HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), OUTLINE_THICKNESS)

def draw(window):
     window.fill(BACKGROUND_COLIR)
     draw_grid(window)
     pygame.display.update()
     

def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    run = False
                    break
            draw(window)
if __name__ == '__main__':
    main(WINDOW)