import matplotlib.pyplot as plt
import numpy as np

from mimic.Annotation import Annotation

class Ellipse(Annotation):


  def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, label: str, confidence : int):
    super().__init__(xmin, xmax, ymin, ymax, label)
    self.confidence :int = confidence
    self.a : float = (xmax - xmin) / 2
    self.b : float = (ymax - ymin) / 2
    self.center_x: float = xmin + self.a
    self.center_y: float = ymin + self.b

  
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
    return (x - self.center_x) ** 2 / self.a ** 2 + (y - self.center_y) ** 2 / self.b ** 2 <= 1

  def plot_shape(self, ax : plt.axes):
    super().plot_shape()
    t = np.linspace(0, 2 * np.pi, 100)
    ax.plot(self.center_x + self.a * np.cos(t), self.center_y + self.b * np.sin(t))
    return ax

  def plot_shape_and_point(self, x : float, y : float):
    """visualise if a point sits inside a polygon"""
    super.plot_shape_and_point(x,y)
    
    ax = plt.axes()
    t = np.linspace(0, 2 * np.pi, 100)
    ax.plot(self.center_x + self.a * np.cos(t), self.center_y + self.b * np.sin(t))
    ax.plot(x, y, 'ro')
    plt.tight_layout()
    plt.show() 
