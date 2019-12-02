import numpy as np
import math

from .ray import Ray
from .objs import AbsObject

class Sphere(AbsObject):

    def __init__(self, center, radius, surface_color):
        self._center = center
        self._radius = radius
        self._surface_color = surface_color


    def center(self):
        return self._center

    def normal(self, ray):
        _, p = self.intersect(ray)

        if p is None:
            return None

        d = p - self.center()
        return Ray(p, d)


    # This methos is besed on the below page.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection
    def intersect(self, ray):
        l = self._center - ray.origin()
        tca = np.dot(l, ray.direction())

        if tca <= 0:
            return None, None

        square_d = np.linalg.norm(l)**2 - tca**2
        if square_d > (self._radius**2):
            return None, None

        thc = np.sqrt(self._radius**2 - square_d)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None, None

        return t0, ray.extension_point(t0)

    # surface
    #  `,       o(origin)
    #    \        ,`
    #     `     ,` |
    #      |  ,`   | ov(orthographic vector)
    #      |,`     v
    #      * ----->*---> n(normal)
    #      |`,rn(resized normal)
    #      |  `,
    #      '    `,
    #     /       `,
    #   ,'       r(reflect)
    #  '
    def reflect(self, ray):
        _, p = self.intersect(ray)
        n = Ray(p, p - self.center())
        cos = np.dot(ray.direction(), n.direction()) * -1
        rn = np.multiply(n.direction(), cos)    # Resize normal

        ov = np.add(ray.direction(), rn)        # Vector between origin ray and normal ray.
        rd = rn + ov                            # Reflect vector direction.

        # Create new ray.
        _, p = self.intersect(ray)
        p2 = np.add(p, np.multiply(rd, 1e-5))   # Move the origin of ray slightly forward.
        return Ray(p2, rd)                      # Reflect ray.

