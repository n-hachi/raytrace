import numpy as np
import math
from .ray import Ray

class Sphere():
    def __init__(self, center, radius, color):
        self._center = center
        self._radius = radius
        self._color = color

    # This methos is besed on the below page.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection
    def intersect(self, ray):
        l = self._center - ray.origin()
        tca = np.dot(l, ray.direction())

        if tca <= 0:
            return None

        square_d = np.linalg.norm(l)**2 - tca**2
        if square_d > (self._radius**2):
            return None

        thc = np.sqrt(self._radius**2 - square_d)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        return ray.extension_point(t0)

    def color(self, ray):
        p = self.intersect(ray)
        d = np.subtract(self._center, p)
        r = Ray(p, d)
        shade = np.dot(ray.direction(), r.direction())
        return tuple(np.floor(np.multiply(self._color, shade)).astype(int))
