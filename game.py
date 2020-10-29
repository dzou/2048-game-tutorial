import pygame
import sys

from grid import Grid, Direction
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

COLORS = {
  0: WHITE,
  2: (203, 199, 198),
  4: (203, 199, 198),
  8: (255, 172, 55),
  16: (255, 144, 55),
  32: (255, 106, 55),
  64: (255, 64, 34),
  128: (255, 220, 32),
  256: (254, 234, 29)
}


pygame.init()

DISPLAY = pygame.display.set_mode((450, 450))
FONT = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

pygame.display.set_caption('2048 Game by dzou')

def draw_square(x, y, value):
  square = pygame.Rect((x, y), (100, 100))

  fill = COLORS.get(value, COLORS[256])
  pygame.draw.rect(DISPLAY, fill, square)

  if value != 0:
    text = FONT.render(str(value), True, WHITE)
    text_rect = text.get_rect(center=square.center)
    DISPLAY.blit(text, text_rect)

def draw_grid(gameGrid):
  arr = gameGrid.get_array()
  for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
      draw_square(10 + 110 * x, 10 + 110 * y, int(arr[y][x]))

if __name__ == "__main__":
  gameGrid = Grid([
    (0, 0, 16, 0),
    (0, 8, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 16, 0)
  ])

  while True:
    shifted_tiles = {}
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          shifted_tiles = gameGrid.shift(Direction.LEFT)
        elif event.key == pygame.K_DOWN:
          shifted_tiles = gameGrid.shift(Direction.DOWN)
        elif event.key == pygame.K_UP:
          shifted_tiles = gameGrid.shift(Direction.UP)
        elif event.key == pygame.K_RIGHT:
          shifted_tiles = gameGrid.shift(Direction.RIGHT)
    
    if shifted_tiles:
      gameGrid.fill_random()
    
    draw_grid(gameGrid)
    pygame.display.update()

    clock.tick(60)
