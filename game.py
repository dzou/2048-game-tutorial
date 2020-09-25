import pygame
import sys

from model.grid import Grid
from pygame.locals import *

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

DISPLAY = pygame.display.set_mode((800, 800))
FONT = pygame.font.SysFont(None, 24)
fpsClock = pygame.time.Clock()

pygame.display.set_caption('2048 Game by dzou')


def draw_square(x, y, value):
  square = pygame.Rect((x, y), (100, 100))
  pygame.draw.rect(DISPLAY, WHITE, square)

  text = FONT.render(value, True, BLACK)
  text_rect = text.get_rect(center=square.center)
  DISPLAY.blit(text, text_rect)

def draw_grid(gameGrid):
  arr = gameGrid.get_array()
  for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
      draw_square(10 + 110 * x, 10 + 110 * y, str(int(arr[y][x])))

if __name__ == "__main__":
  grid2048 = Grid()

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    
    draw_grid(grid2048)
    pygame.display.update()

    fpsClock.tick(60)
