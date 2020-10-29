import numpy
import random

from enum import Enum

class Grid:

  def __init__(self, tuples=None):
    if tuples:
      self.grid = numpy.array(tuples)
    else:
      self.grid = numpy.zeros((4, 4))
  
  def get_array(self):
    return self.grid

  def fill_random(self):
    empty_cells = []
    for p, value in numpy.ndenumerate(self.grid):
      if value == 0:
        empty_cells.append(p)
    
    if empty_cells:
      cell = random.choice(empty_cells)
      if random.random() > 0.1:
        val = 2
      else:
        val = 4
      self.grid[cell] = val
      print("filled " + str(cell) + " to: " + str(val))

  def shift(self, dir):
    size = len(self.grid)

    shifted_tiles = dict()
    merged = set()

    if dir == Direction.UP:
      for y in range(size):
        for x in range(size):
          dest = self.shift_tile(x, y, dir, merged)
          if dest:
            shifted_tiles[(x, y)] = dest
    elif dir == Direction.DOWN:
      for y in range(size):
        for x in range(size):
          dest = self.shift_tile(x, size - 1 - y, dir, merged)
          if dest:
            shifted_tiles[(x, size - 1 - y)] = dest
    elif dir == Direction.RIGHT:
      for x in range(size):
        for y in range(size):
          dest = self.shift_tile(size - 1 - x, y, dir, merged)
          if dest:
            shifted_tiles[(size - 1 - x, y)] = dest
    elif dir == Direction.LEFT:
      for x in range(size):
        for y in range(size):
          dest = self.shift_tile(x, y, dir, merged)
          if dest:
            shifted_tiles[(x, y)] = dest

    return shifted_tiles

  def shift_tile(self, x, y, dir, merged):
    curr_tile = self.grid[y][x]

    if curr_tile == 0:
      return

    prev = (x, y)
    next = (x + dir.value[0], y + dir.value[1])

    while self.in_bounds(next[0], next[1]) and next not in merged:
      next_tile = self.grid[next[1]][next[0]]

      if next_tile == 0:
        prev = next
        next = (next[0] + dir.value[0], next[1] + dir.value[1])
      elif next_tile != curr_tile:
        break
      elif next_tile == curr_tile:
        prev = next
        curr_tile *= 2
        merged.add(prev)
        break

    if (x, y) != prev:
      self.grid[prev[1]][prev[0]] = curr_tile
      self.grid[y][x] = 0
      return prev
    else:
      return None

  def in_bounds(self, x, y):
    return x >= 0 and y >= 0 and x < self.grid.shape[1] and y < self.grid.shape[0]

  def __str__(self):
    return str(self.grid)

    
class Direction(Enum):
  UP = (0, -1)
  DOWN = (0, 1)
  LEFT = (-1, 0)
  RIGHT = (1, 0)

if __name__ == "__main__":
  grid = Grid([
    (0, 0, 16, 0),
    (0, 8, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 16, 0)
  ])
  print(grid)

  print(grid.shift(Direction.DOWN))
  print(grid.fill_random())
  print(grid.fill_random())
  print(grid.fill_random())
  print(grid.fill_random())
  print(grid.fill_random())
  print(grid.fill_random())

  print(grid)
