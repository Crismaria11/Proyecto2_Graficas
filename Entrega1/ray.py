from lib import *
from material import *
from sphere import *
from math import pi, tan

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

class Raycaster(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.background_color = color(0, 0, 0)
    self.scene = []
    self.glClear()

  def glClear(self):
    self.pixels = [
      [self.background_color for x in range(self.width)]
      for y in range(self.height)
    ]

  def finish(self, filename):
    f = open(filename, 'bw')

    #file header
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))


    # image loader
    f.write(dword(40))
    f.write(dword(self.width))
    f.write(dword(self.height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))


    # pixel data
    for x in range(self.width):
      for y in range(self.height):
        f.write(self.pixels[x][y])


    f.close()

  
  def point(self, x, y, color = None):
    try: 
      self.pixels[y][x] = color or self.background_color
    except:
      pass

  def scene_intersect(self, orig, direction):
    for obj in self.scene:
      if obj.ray_intersect(orig, direction):
        return obj.material
    return None

  def cast_ray(self, orig, direction):
    impacted_material = self.scene_intersect(orig, direction)
    if impacted_material:
      return impacted_material.diffuse
    else:
      return color(0, 0, 0)

  def render(self):
    fov = int(pi/2)

    for y in range(self.height):
      for x in range(self.width):
        i = (2 * (x + 0.5)/self.width - 1) * self.width / self.height * tan(fov/2)
        j = (1 - 2 * (y + 0.5)/self.height) * tan(fov/2)
        direction = norm(V3(i, j, -1))
        self.pixels[y][x] = self.cast_ray(V3(0, 0, 0), direction)

r = Raycaster(1000, 1000)
r.scene = [
  # pupilas
  Sphere(V3(-0.65, -4.35, -10), 0.2, piedra),
  Sphere(V3(0.65, -4.35, -10), 0.2, piedra),
  # ojos
  Sphere(V3(-0.65, -4.35, -10), 0.4, pupila),
  Sphere(V3(0.65, -4.35, -10), 0.4, pupila),
  # boca
  Sphere(V3(-0.7, -3.20, -10), 0.2, piedra),
  Sphere(V3(0.7, -3.20, -10), 0.2, piedra),
  Sphere(V3(-0.30, -3.0, -10), 0.2, piedra),
  Sphere(V3(0.30, -3.0, -10), 0.2, piedra),
  # botones
  Sphere(V3(0, -1, -10), 0.55, piedra),
  Sphere(V3(0, 1, -10), 0.55, piedra),
  Sphere(V3(0, 3, -10), 0.55, piedra),
  # nariz
  Sphere(V3(0, -3.7, -10), 0.3, nariz),
  # cuerpo
  Sphere(V3(0, 2.5, -10), 2.5, nieve),
  Sphere(V3(0, -1, -10), 2, nieve),
  Sphere(V3(0, -3.5, -10), 1.5, nieve)
  
]
r.render()
r.finish('out.bmp')