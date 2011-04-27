
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
  
  def __init__(self, layout_fname):
    """
    empty_spaces is implemented using a set of tuples
    """
    self.empty_spaces = set()
    self.start = self.target = None
    grid = []
    with open(layout_fname, 'r') as layout_file:
      for line in layout_file:
        # grid.append([int(elem) for elem in list(line.strip())])
        if line.strip():
          grid.append(list(line.strip()))
    self.height = len(grid)
    self.width = len(grid[0])
    for row in xrange(len(grid)):
      for col in xrange(len(grid[row])):
        if grid[row][col] != '1':
          self.empty_spaces.add((row,col))
          if grid[row][col] == 's':
            if self.start:
              raise RuntimeError('More than one start location in maze')
            self.start = (row, col)
          elif grid[row][col] == 't':
            if self.target:
              raise RuntimeError('More than one target location in maze')
            self.target = (row, col)
    if not self.start or not self.target:
      raise RuntimeError('Start and target location not in maze')
  
  def get_neighbors(self, node):
    pass
  
  def is_exit(self, node):
    pass
  
  def have_visited(self, node):
    pass
  
  def __str__(self):
    grid = ''
    for row in xrange(self.height):
      for col in xrange(self.width):
        if (row,col) in self.empty_spaces:
          if (row,col) == self.start:
            grid += 's'
          elif (row,col) == self.target:
            grid += 't'
          else:
            grid += '0'
        else:
          grid += '1'
      grid += "\n"
    return grid

def test_construction(maze, test_layout_fname):
  with open(test_layout_fname, 'r') as layout_file:
    assert str(maze).strip() == layout_file.read().strip()

def test_maze():
  if len(sys.argv) == 2:
    test_layout_fname = sys.argv[1]
  else:
    test_layout_fname = 'sample_input'
  m = Maze(test_layout_fname)
  test_construction(m, test_layout_fname)
  print "Tests passed"

if __name__ == '__main__':
  test_maze()

