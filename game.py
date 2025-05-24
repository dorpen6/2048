## RULES OF THE GAME
## 4X4 GRIDS = MAX 16 TILES
## EVERY TIME WE MOVE => WE ADD 1 TILE TO THE GAME
## 2 2 => 4
## WHEN THE TILES HAVE SAME VALUES AND THEY HIT EACH OTHER, SUM THEM => 4 4 = 8, 8 8 = 16... ETC.
## YOU WILL LOOSE THE GAME IF THERE IS NO MORE ROOM ON THE GAME TO ADD MORE TILES AND YOU CAN'T MERGE ANY OF THEM TOGETHER.

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
    COLORS = [
        (255, 248, 220),  # Cornsilk
        (250, 235, 190),  # Light tan
        (255, 200, 124),  # Apricot
        (255, 165, 79),   # Light pumpkin
        (255, 140, 60),   # Tangerine
        (255, 105, 35),   # Sunset orange
        (255, 220, 120),  # Pale gold
        (255, 210, 90),   # Goldenrod
        (255, 200, 60),   # Amber
    ]

    def __init__(self, value, row, col):
         self.value = value
         self.row = row
         self.col = col
         self.x = col * RECT_WIDTH
         self.y = row * RECT_HEIGHT

    def get_color(self):
         pass
    
    def draw(self, window):
         pass
    
    def move(self, delta):
         pass
    
    def set_position(self):
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