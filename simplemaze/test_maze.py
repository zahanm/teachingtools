
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
    with open(sys.argv[1], 'r') as test_layout_file:
      test_layout = test_layout_file.read().strip()
  else:
    test_layout = sample_layout
  m = Maze(test_layout)
  assert str(m).strip() == test_layout.strip()

def test_neighbors():
  m = Maze(sample_layout)
  ns = m.get_neighbors(1,1)
  assert len(ns) == 2 # unituitive method for set size
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
  test_construction()
  test_neighbors()
  print "Tests passed"

if __name__ == '__main__':
  main()

