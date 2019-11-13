import numpy as np
import math
from .ray import Ray

class Circle():
    def __init__(self, center, radius, normal, color):
        self._center = center
        self._radius = radius
        self._normal = normal
        self._color = color

    # This method was referred to the following page.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-plane-and-ray-disk-intersection
    def intersect(self, ray):
        d = np.dot(ray.direction(), self._normal) # Denominator

        # In case, ray is parallel to the circle surface.
        if abs(d) < 1e-5:
            return None, None

        l0 = ray.origin()
        n = np.dot((self._center - l0), self._normal) # Numerator
        t = n / d

        # In case, cirle is on opposite side of ray orientation.
        if t < 0:
            return None, None

        p = ray.extension_point(t)
        g = np.linalg.norm(p - self._center)
        if g > self._radius:
            return None, None

        return t, p

    def color(self, ray):
        shade = abs(np.dot(ray.direction(), self._normal))
        return tuple(np.floor(np.multiply(self._color, shade)).astype(int))
