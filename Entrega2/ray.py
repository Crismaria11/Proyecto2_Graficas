from lib import *
from material import *
from sphere import *
from math import pi, tan
from intersect import *
from light import *
import random

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
BACKGROUND = color(200, 200, 190)

class Raycaster(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.background_color = BACKGROUND
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
        f.write(self.pixels[x][y].toBytes())


    f.close()

  
  def point(self, x, y, color = None):
    try: 
      self.pixels[y][x] = color or self.background_color
    except:
      pass

  def scene_intersect(self, orig, direction):
    zbuffer = float('inf')

    material = None
    intersect = None

    for obj in self.scene:
      hit = obj.ray_intersect(orig, direction)
      if hit is not None:
        if hit.distance < zbuffer:
          zbuffer = hit.distance
          material = obj.material
          intersect = hit

    return material, intersect

  def cast_ray(self, orig, direction):
    material, intersect = self.scene_intersect(orig, direction)

    if material is None:
      return self.background_color

    light_dir = norm(sub(self.light.position, intersect.point))
    light_distance = length(sub(self.light.position, intersect.point))

    offset_normal = mul(intersect.normal, 1.1)
    shadow_orig = sub(intersect.point, offset_normal) if dot(light_dir, intersect.normal) < 0 else sum(intersect.point, offset_normal)
    shadow_material, shadow_intersect = self.scene_intersect(shadow_orig, light_dir)
    shadow_intensity = 0

    if shadow_material and length(sub(shadow_intersect.point, shadow_orig)) < light_distance:
      shadow_intensity = 0.9

    intensity = self.light.intensity * max(0, dot(light_dir, intersect.normal)) * (1 - shadow_intensity)

    reflection = reflect(light_dir, intersect.normal)
    specular_intensity = self.light.intensity * (
      max(0, -dot(reflection, direction))**material.spec
    )

    diffuse = material.diffuse * intensity * material.albedo[0]
    specular = color(255, 255, 255) * specular_intensity * material.albedo[1]
    return diffuse + specular

  def render(self):
    fov = int(pi/2)
    for y in range(self.height):
      for x in range(self.width):
        i =  (2 * (x + 0.5)/self.width - 1) * tan(fov/2) * self.width/self.height
        j =  (2 * (y + 0.5)/self.height - 1) * tan(fov/2)
        direction = norm(V3(i, j, -1))
        self.pixels[y][x] = self.cast_ray(V3(0,0,0), direction)

r = Raycaster(2000, 2000)

r.light = Light(
  position=V3(0, 0, 20),
  intensity=1.5
)

r.scene = [
  # esfera de navidad
  Sphere(V3(-2.5, -1, -10), 2, navidad1),
  Sphere(V3(2.5, -1, -10), 2, navidad2),
  # cabeza
  Sphere(V3(-2.5, 2, -10), 1.5, cuerpo1),
  Sphere(V3(2.5, 2, -10), 1.5, cuerpo2),
  # orejas
  Sphere(V3(-3.5, 3.5, -10), 0.6, cuerpo1),
  Sphere(V3(-1.5, 3.5, -10), 0.6, cuerpo1),
  Sphere(V3(3.5, 3.5, -10), 0.6, cuerpo2),
  Sphere(V3(1.5, 3.5, -10), 0.6, cuerpo2),
  # brazos
  Sphere(V3(-3.5, 0, -8), 0.6, cuerpo1),
  Sphere(V3(3.5, 0, -8), 0.6, cuerpo2),
  Sphere(V3(-1, 0, -8), 0.6, cuerpo1),
  Sphere(V3(1, 0, -8), 0.6, cuerpo2),
  # piernas
  Sphere(V3(-3.5, -2, -8), 0.6, cuerpo1),
  Sphere(V3(3.5, -2, -8), 0.6, cuerpo2),
  Sphere(V3(-1, -2, -8), 0.6, cuerpo1),
  Sphere(V3(1, -2, -8), 0.6, cuerpo2),
  # nariz
  Sphere(V3(-2.5, 1.5, -8.5), 0.6, cuerpo1),
  Sphere(V3(2.5, 1.5, -8.5), 0.6, cuerpo2),
  # punta nariz
  Sphere(V3(-2.3, 1.25, -7.5), 0.1, negro),
  Sphere(V3(2.3, 1.25, -7.5), 0.1, negro),
  # ojos
  Sphere(V3(-3, 2.4, -8.5), 0.2, negro),
  Sphere(V3(-2, 2.4, -8.5), 0.2, negro),
  Sphere(V3(3, 2.4, -8.5), 0.2, negro),
  Sphere(V3(2, 2.4, -8.5), 0.2, negro),

]
r.render()
r.finish('out.bmp')