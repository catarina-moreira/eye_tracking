from abc import ABC, abstractmethod

import numpy as np
import math


class Annotation(ABC):

  def __init__(self, xmin : float, xmax : float, ymin : float, ymax : float, label : str) :
    super().__init__()
    self.xmin = xmin
    self.xmax = xmax
    self.ymin = ymin
    self.ymax = ymax
    self.label = label

    self.width = np.abs(xmax - xmin)
    self.height = np.abs(ymax - ymin)
    self.center = [self.width/2, self.height/2 ]

  @abstractmethod
  def process_shape(self):
    """Returns a matplotlip patch which can be overlayed on an Xray image"""
    pass

  @abstractmethod
  def area(self):
    """Computes the area of a given polygon"""
    pass

  @abstractmethod
  def perimeter(self):
    """Computes the perimeter of a given polygon"""
    pass

  @abstractmethod
  def is_point_inside_shape(self, x:float, y:float):
    """checks whether a coordinate (x,y) sits inside of a polygon"""
    pass

  @abstractmethod
  def plot_shape_and_point(self, x : float, y : float):
    """plots a shape and point"""
    pass

  @abstractmethod
  def plot_shape(self):
    pass


  def getCoordinates(self):
    return [ self.xmin, self.xmax, self.ymin, self.ymax]

  def getXmin(self):
    return self.xmin
  
  def getXmax(self):
    return self.xmax 

  def getYmin(self):
    return self.ymin

  def getYmax(self):
    return self.ymax

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height
  
  def getLabel(self):
    return self.label

  def setXmin(self, new_xmin : float):
    self.xmin = new_xmin
  
  def setXmax(self, new_xmax : float):
    self.xmax = new_xmax

  def setYmin(self, new_ymin : float):
    self.ymin = new_ymin

  def setYmax(self, new_ymax : float):
    self.ymax = new_ymax

  def setWidth(self, new_width : float):
    self.width = new_width

  def setHeight(self, new_height : float):
    self.height = new_height
  
  def setLabel(self, new_label : str):
    self.label = new_label


