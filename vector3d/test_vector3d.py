#!/usr/bin/env python

from nose.tools import *
from vector3d import Vector3d

class TestVector3d:
  
  def __init__(self):
    self.a = Vector3d(1,2,3)
    self.b = Vector3d(2,3,4)

  def test_init(self):
    eq_(self.a, [1,2,3])
  
  def test_addition(self):
    eq_(self.a + self.b, [3,5,7])
  
  @raises(AttributeError)
  def test_bad_addition(self):
    eq_(self.a+1, [1,2,3])
  
  def test_subtraction(self):
    eq_(self.b - self.a, [1,1,1])
  
  def test_scalar_mul(self):
    assert_equal(self.a*2, [2,4,6])
  
  def test_dot_product(self):
    assert_equal(self.a.dot(self.b), [2,6,12])
  
  def test_cross_product(self):
    assert_equal(self.a.cross(self.b), [-1,2,-1])

if __name__ == '__main__':
  print("Use nosetests to run this script")

