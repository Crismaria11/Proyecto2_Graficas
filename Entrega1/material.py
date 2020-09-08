from lib import color
# material

class Material(object):
  def __init__(self, diffuse):
    self.diffuse = diffuse

piedra = Material(diffuse=color(0, 0, 0))
nieve = Material(diffuse=color(255, 255, 255))
pupila = Material(diffuse=color(155, 155, 155))
nariz = Material(diffuse=color(239, 127, 26))