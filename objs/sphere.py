import numpy as np
import math

class Sphere():
    def __init__(self, center, radius):
        self._center = center
        self._radius = radius

    # This methos is besed on the below page.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection
    def intersect(self, ray):
        l = self._center - ray.origin()
        tca = np.dot(l, ray.direction())

        if tca <= 0:
            return False

        square_d = np.linalg.norm(l)**2 - tca**2
        if square_d > (self._radius**2):
            return False

        thc = np.sqrt(self._radius**2 - square_d)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return False

        return True
