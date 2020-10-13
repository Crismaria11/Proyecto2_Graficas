from lib import color
# material

class Material(object):
  def __init__(self, diffuse, albedo, spec, refraction_index):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
    self.refraction_index = refraction_index


cuerpo1 = Material(diffuse=color(255, 255, 255), albedo=(0.6, 0.3, 0.1), spec=5, refraction_index = 0)
cuerpo2 = Material(diffuse=color(194, 155, 97), albedo=(0.6, 0.3, 0.1), spec=5, refraction_index = 0)

navidad1 = Material(diffuse=color(244, 244, 244), albedo=(0.6, 0.3, 0.1), spec=5, refraction_index = 0)
navidad2 = Material(diffuse=color(255, 0, 0), albedo=(0.6, 0.3, 0.1), spec=5, refraction_index = 0)


negro = Material(diffuse=color(0, 0, 0), albedo=(0.5, 0.5, 0.5), spec=5, refraction_index = 0)
cafe = Material(diffuse=color(128, 64, 0), albedo=(0.5, 0.5, 0.5), spec=5, refraction_index=0)
cielo = Material(diffuse=color(135, 206, 250), albedo=(0.5, 0.5), spec=5, refraction_index=0)
sol = Material(diffuse=color(243, 159, 24), albedo=(0.5, 0.5, 0.5), spec=50, refraction_index=0)
casa = Material(diffuse=color(255, 255, 255), albedo=(0.9, 0.9, 0.9), spec=5, refraction_index = 0)
nieve = Material(diffuse=color(240, 238, 212), albedo=(0.9, 0.9, 0.9), spec=5, refraction_index = 0)
hojas = Material(diffuse=color(45, 87, 44), albedo=(0.9, 0.9, 0.9), spec=5, refraction_index = 0)
crema = Material(diffuse=color(249, 228, 183), albedo=(0.9, 0.9, 0.9), spec=5, refraction_index = 0)
luna = Material(diffuse=color(233, 227, 155), albedo=(0.9, 0.9, 0.9), spec=5, refraction_index = 0)
nube = Material(diffuse=color(36, 68, 191), albedo=(0.9, 0.9, 0.9), spec=50, refraction_index = 0)

pupila = Material(diffuse=color(155, 155, 155), albedo=(0.3, 0.3), spec=13, refraction_index = 0)
nariz = Material(diffuse=color(239, 127, 26), albedo=(0.2, 0.2), spec=12, refraction_index = 0)
