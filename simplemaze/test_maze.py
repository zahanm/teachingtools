
#
# Unit tests to test Maze
# Also compatible with ~> nosetests
#

import sys

from maze import Maze

sample_layout = \
"""
1s1100
100101
110001
00010t
011111
"""

def test_construction():
  if len(sys.argv) == 2:
    parsed_info = Maze.parse_layout(sys.argv[1])
    test_layout = parsed_info[0]
    test_info = parsed_info[1]
  else:
    test_layout = sample_layout
    test_info = None
  m = Maze(test_layout, test_info)
  assert str(m).strip() == test_layout.strip()

def test_neighbors():
  m = Maze(sample_layout)
  ns = m.get_neighbors(1,1)
  assert len(ns) == 2 # unintuitive method for set size
  assert (1,2) in ns
  assert (0,1) in ns
  ns = m.get_neighbors(4,0)
  assert ns == set([(3,0)])

def test_visiting():
  m = Maze(sample_layout)
  assert not m.visit(3,1)
  assert m.visited(3,1)
  assert m.visit(3,5)

def main():
  """
  Runs all tests. A preferable way to run them is with nosetests
  """
  test_construction()
  test_neighbors()
  test_visiting()
  print "Tests passed"

if __name__ == '__main__':
  main()

