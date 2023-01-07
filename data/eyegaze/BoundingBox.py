
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from mimic.Annotation import Annotation
from Constants import Constants as c


class BoundingBox(Annotation):

  def __init__(self, xmin : float, xmax : float, ymin : float, ymax : float, label : str):
    super().__init__(xmin, xmax, ymin, ymax, label)

  def process_shape(self):
    """returns a patch with a polygon"""
    super().process_shape()
    color = c.COLOR_MAP[self.label.upper()]
    polygon = Rectangle((self.xmin, self.ymin), super().width, super().height,\
                          linewidth=3, edgecolor=color, facecolor='none', label = self.label)
    return polygon

  def area(self):
    """computes the area of a polygon"""
    super().area()
    return super().getWidth()*super().getHeight()

  def perimeter(self):
    """Computes the perimeter of a polygon"""
    super().perimeter()
    return super().getWidth()*2 + super().getHeight()*2

  def is_point_inside_shape(self, x: float, y: float):
    """returns a Boolean that checks whether a point (x,y) sits inside a bounding box"""
    return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax

  def plot_shape(self, ax : plt.axes):
    """plots a bounding box in a given plt axes"""
    super().plot_shape()
    ax.plot([self.xmin, self.xmax, self.xmax, self.xmin, self.xmin], \
             [self.ymin, self.ymin, self.ymax, self.ymax, self.ymin], c = c.COLOR_MAP[self.label.upper()])
    return ax
    
  def plot_shape_and_point(self, x : float, y : float, xray_path = None):
    """visualise if a point sits inside a polygon"""
    super().plot_shape_and_point(x,y)

    ax = plt.axes()
    if xray_path:
      img = plt.imread( xray_path )
      ax.imshow(img, cmap=plt.cm.bone)  
      plt.xlim([0, img.shape[1]])
      plt.ylim([0, img.shape[0]])
      ax.invert_yaxis()
    else:
      plt.xlim([0, 2700])
      plt.ylim([0, 3000])

    ax.plot([self.xmin, self.xmax, self.xmax, self.xmin, self.xmin], \
             [self.ymin, self.ymin, self.ymax, self.ymax, self.ymin], c = c.COLOR_MAP[self.label.upper()])
    ax.plot(x, y, 'ro')
    ax.text((self.xmin + self.xmax) / 2, (self.ymin - 50), self.label, ha='center', va='center', c = c.COLOR_MAP[self.label.upper()])
    plt.tight_layout()
    plt.show()

  def getXmax(self):
    return super().getXmax()

  def getXmin(self):
    return super().getXmin()
  
  def getYmax(self):
    return super().getYmax()
  
  def getYmin(self):
    return super().getYmin()


