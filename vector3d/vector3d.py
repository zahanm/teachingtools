#!/usr/bin/env python

# The following is how you write documentation for your work in Python.
# Now, if you invoke
# >> help(Vector3d)
# The string in triple quotes will be displayed as help.

import numpy as np

class Vector3d:
  """
    A 3D Vector in Cartesian coordinates to handle all sorts of operations.
  """
  
  def __init__(self, *args):
    """
      The equivalent of a constructor in Python, this is invoked when you create
      a new object.
    """
    if len(args) == 3:
      self.xyz = np.array(args, dtype='f')
    elif len(args) == 1:
      self.xyz = np.array(args[0], dtype='f')
    else:
      raise TypeError("__init__() takes either 2 or 4 arguments ({0} given)"\
      .format(len(args)))
  
  def dot(self, other):
    """
      Scalar dot product of vectors
      Differing multiplication to np.array pairwise method
      See __eq__()
    """
    return Vector3d(self.xyz * other.xyz)
  
  def cross(self, other):
    """
      Cross product of vectors
      Had to do this by hand
    """
    x = self.xyz[1]*other.xyz[2] - self.xyz[2]*other.xyz[1]
    y = self.xyz[2]*other.xyz[0] - self.xyz[0]*other.xyz[2]
    z = self.xyz[0]*other.xyz[1] - self.xyz[1]*other.xyz[0]
    return Vector3d(x,y,z)
  
  # Here start all the cool internal methods that make operators work seamlessly
  
  def __eq__(self, other):
    """
      Differing the actual equality comparison to the np.array equality method
      That function does a pairwise comparison and returns an array of booleans
      The .all() method ensures that all elements are equal
    """
    return (other == self.xyz).all()
  
  def __add__(self, other):
    """
      Again, differing addition to np.array pairwise method
    """
    return Vector3d(self.xyz + other.xyz)
  
  def __sub__(self, other):
    """
      Again, differing subtraction to np.array pairwise method
    """
    return Vector3d(self.xyz - other.xyz)
  
  def __mul__(self, other):
    """
      This is for the scalar multiple of a vector
    """
    return Vector3d(self.xyz * other)
  
  def __str__(self):
    """
      This is invoked when you call str(obj)
    """
    return "[{0}, {1}, {2}]".format(self.xyz[0], self.xyz[1], self.xyz[2])
  
  def __repr__(self):
    """
      This is what is displayed by default when you 'inspect' an object
      When you display an object in the command line interpreter
      >> repr(obj)
      is called.
    """
    return "Vector3d( {0} )".format(self.xyz)
  
  # And this is static method in case you ever have to define one
  
  @staticmethod
  def num_dim():
    """
      The equivalent of 'static' methods in Java.
      The decorator is necessary.
      Notice, no 'self' argument as no object is associated with the method.
    """
    return 3

if __name__ == '__main__':
  print 'This script is not meant to be run directly'

