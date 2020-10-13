from lib import *
from sphere import *
import math

class Cone(object):
  def __init__(self, radius, height, position, material):
    self.radius = radius
    self.height = height
    self.position = position
    self.material = material

  def ray_intersect(self, origin, direction):
    A = origin.x - self.position.x
    B = origin.z - self.position.z
    D = self.height - origin.y + self.position.y
    
    tan = (self.radius/self.height)**2
    
    a = (direction.x * direction.x) + (direction.z * direction.z) - (tan*(direction.y * direction.y))
    b = (2 * A * direction.x) + (2 * B * direction.z) + (2 * tan * D * direction.y)
    c = (A * A) + (B * B) - (tan * (D * D))
    
    delta = b * b - 4 * (a * c)
    if(abs(delta) < 0.001):
      return None
    if(delta < 0.0):
      return None
    
    t1 = (-b - math.sqrt(delta)) / (2 * a)
    t2 = (-b + math.sqrt(delta)) / (2 * a)
        
    t = t1
    if (t1 > t2):
      t = t2
    
    r = origin.y + t * direction.y
    
    if ((r > self.position.y) and (r < self.position.y + self.height)):
      hit = sum(origin, mul(direction, t))
      normal = norm(sub(hit, self.position))
      return Intersect(
        distance=t,
        point=hit,
        normal=normal
      )
    else:
     return None