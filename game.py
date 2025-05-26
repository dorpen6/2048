## RULES OF THE GAME
## 4X4 GRIDS = MAX 16 TILES
## EVERY TIME WE MOVE => WE ADD 1 TILE TO THE GAME
## 2 2 => 4
## WHEN THE TILES HAVE SAME VALUES AND THEY HIT EACH OTHER, SUM THEM => 4 4 = 8, 8 8 = 16... ETC.
## YOU WILL LOOSE THE GAME IF THERE IS NO MORE ROOM ON THE GAME TO ADD MORE TILES AND YOU CAN'T MERGE ANY OF THEM TOGETHER.

import pygame   # create games and multimedia applications
import random   # generate random numbers
import math     # provides mathematical functions

pygame.init()   # initialize all the different features that we need

FPS = 60        # frames per second, dictade how quickly the game is running

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS    # 200 PX
RECT_WIDTH = WIDTH // COLS      # 200 PX

OUTLINE_COLOR = (187, 173, 160) # GREY
OUTLINE_THICKNESS = 10             
BACKGROUND_COLIR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VELOCITY = 20 # SPEED OF THE TILES WHICH WILL MOVE 20PX PER SECOND

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
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
          color_index = (math.log2(self.value)) - 1 # This line calculates color_index by taking the base-2 logarithm of self.value and subtracting 1,  used to map powers of 2 (like 2, 4, 8...) to sequential indices starting from 0.
          color = self.COLORS[color_index]
          return color
    
    def draw(self, window):
          color = self.get_color()
          pygame.draw.rect(window, colorm (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

          text = FONT.render(str(self.value), 1, FONT_COLOR)
          window.blit(
               text,
               (
                    self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                    self.y + (RECT_HEIGHT / 2 - text.get_height() / 2),
               ),
          )
         
    
    def move(self, delta):
         pass
    
    def set_position(self):
         pass
    




def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    
    for column in range(1, COLS):
        x = column * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

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