import numpy as np
import math
from .sphere import Sphere
from .ray import Ray

class CheckerdSphere(Sphere):
    def color(self, ray, objects, lights):
        c = super().color(ray, objects, lights)

        _, p = super().intersect(ray)
        d = np.subtract(p, self._center)
        ray2 = Ray(p, d)

        v = ray2.direction()
        phy = math.atan2(v[2], v[0])
        thete = math.acos(v[1])
        
        x = int((phy + math.pi) * 8 / math.pi)
        y = int(thete * 8 / math.pi)

        is_color = 1 if ((x % 2) ^ (y % 2)) else 0.1

        return np.multiply(c, is_color)
