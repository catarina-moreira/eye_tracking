import matplotlib.pyplot as plt
import numpy as np

from mimic.Annotation import Annotation

class Ellipse(Annotation):


  def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, label: str, confidence : int):
    super().__init__(xmin, xmax, ymin, ymax, label)
    self.confidence :int = confidence

  
  def process_shape(self):
    """returns a patch with a polygon"""
    return super().process_shape()

  def area(self):
    """computes the area of a polygon"""
    return super().area()

  def perimeter(self):
    """Computes the perimeter of a polygon"""
    return super().perimeter()

  def is_point_inside_shape(self, x: float, y: float):
    """returns a Boolean that checks whether a point (x,y) sits inside a polygon"""
    super().is_point_inside_shape(x,y)
    a = (self.xmax - self.xmin) / 2 # get minor axis
    b = (self.ymax - self.ymin) / 2 # get major axis
    
    center_x = self.xmin + a
    center_y = self.xmax + b
    return (x - center_x) ** 2 / a ** 2 + (y - center_y) ** 2 / b ** 2 <= 1

  def plot_shape_and_point(self, x : float, y : float):
    """visualise if a point sits inside a polygon"""
    super.plot_shape_and_point(x,y)
    a = (self.xmax - self.xmin) / 2
    b = (self.ymax - self.ymin) / 2
    center_x = self.xmin + a
    center_y = self.ymin + b

    t = np.linspace(0, 2 * np.pi, 100)
    plt.plot(center_x + a * np.cos(t), center_y + b * np.sin(t))
    plt.plot(x, y, 'ro')
    plt.axis('equal')
    plt.show() 
