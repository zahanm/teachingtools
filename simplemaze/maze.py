
import sys, os

class Node:
  """
  Location - details
  """
  def __init__(self, r, c, t):
    self.row = r
    self.col = c
    self.type = t


class Maze:
  """
  'Black box' used to hide details of graph used
  Exercise is to use queues and BFS to find shortest path to exit
  
  Assuming standard euclidean geometry and a flat maze
  """
  
  def __init__(self, layout):
    """
    empty_spaces is implemented using a set of tuples
    """
    self._start = self._target = None
    empty_spaces = set()
    grid = []
    for line in layout.split("\n"):
      if line.strip():
        grid.append(list(line.strip()))
    self._height = len(grid)
    self._width = len(grid[0])
    for row in xrange(len(grid)):
      for col in xrange(len(grid[row])):
        if grid[row][col] != '1':
          empty_spaces.add((row,col))
          if grid[row][col] == 's':
            if self._start:
              raise RuntimeError('More than one start location in maze')
            self._start = (row, col)
          elif grid[row][col] == 't':
            if self._target:
              raise RuntimeError('More than one target location in maze')
            self._target = (row, col)
    if not self._start or not self._target:
      raise RuntimeError('Start and target location not in maze')
    self._empty_spaces = frozenset(empty_spaces)
    self._visited = set([self._start]) # currently at self._start
  
  def get_neighbors(self, row, col):
    """
    returns the set of all valid empty neighbour locations
    """
    neighbors = set()
    for d in [-1,1]:
      if row+d >= 0 and row+d < self._height and \
      (row+d,col) in self._empty_spaces:
        neighbors.add((row+d,col))
      if col+d >= 0 and col+d < self._width and \
      (row,col+d) in self._empty_spaces:
        neighbors.add((row,col+d))
    return neighbors
  
  def visit(self, row, col):
    """
    returns whether this node is the exit, and marks it as visited
    """
    self._visited.add((row,col))
    return (row,col) == self._target
  
  def visited(self, row, col):
    """
    returns whether you have visited this node before
    """
    return (row, col) in self._visited
  
  def __str__(self):
    grid = ''
    for row in xrange(self._height):
      for col in xrange(self._width):
        if (row,col) in self._empty_spaces:
          if (row,col) == self._start:
            grid += 's'
          elif (row,col) == self._target:
            grid += 't'
          else:
            grid += '0'
        else:
          grid += '1'
      grid += "\n"
    return grid

if __name__ == '__main__':
  print("Do not call this module directly.")
  print("Test using test_maze.py or nosetests")

