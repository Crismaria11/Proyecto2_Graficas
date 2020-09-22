from lib import color
# material

class Material(object):
  def __init__(self, diffuse, albedo, spec):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec


cuerpo1 = Material(diffuse=color(255, 255, 255), albedo=(0.6, 0.3, 0.1), spec=5)
cuerpo2 = Material(diffuse=color(194, 155, 97), albedo=(0.6, 0.3, 0.1), spec=5)

navidad1 = Material(diffuse=color(244, 244, 244), albedo=(0.6, 0.3, 0.1), spec=5)
navidad2 = Material(diffuse=color(255, 0, 0), albedo=(0.6, 0.3, 0.1), spec=5)


negro = Material(diffuse=color(0, 0, 0), albedo=(0.5, 0.5), spec=15)
nieve = Material(diffuse=color(255, 255, 255), albedo=(0.4, 0.4), spec=14)
pupila = Material(diffuse=color(155, 155, 155), albedo=(0.3, 0.3), spec=13)
nariz = Material(diffuse=color(239, 127, 26), albedo=(0.2, 0.2), spec=12)
