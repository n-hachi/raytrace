import numpy as np
import math
from .ray import Ray
from .circle import Circle

class ReflectiveCircle(Circle):
    IsReflective = True

    def color(self, ray, objects, lights):
        r = self.reflect(ray)                       # Reflect ray.
        c = r.color(objects, lights)

        # Generate ray between intersect point and light source.
        coefficient = 0
        for l in lights:
            r2 = Ray(r.origin(), l.center() - r.origin())
            o, _, _ = r2.intersect(objects)

            if o is not None:
                continue
            dots = np.dot(r2.direction(), r.direction())
            coefficient += max(0, dots)

        coefficient = min(1, coefficient) * 0.8
        return np.multiply(r.color(objects, lights), coefficient)

