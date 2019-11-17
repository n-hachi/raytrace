import numpy as np
import math
from .ray import Ray
from .circle import Circle

class ReflectiveCircle(Circle):
    IsReflective = True

    # surface
    #   |     o(origin)
    #   |      ,`
    #   |    ,` |
    #   |  ,`   | ov(orthographic vector)
    #   |,`     v
    #   * ----->*---> n(normal)
    #   |`,rn(resized normal)
    #   |  `,
    #   |    `,
    #   |      `,
    #   |     r(reflect)
    #
    def color(self, ray, objects):
        n = self._normal
        cos = np.dot(ray.direction(), n) * -1   # Cosine
        rn = np.multiply(n, cos)                # Resize normal

        ov = np.add(ray.direction(), rn)        # Vector between origin ray and normal ray.
        rd = rn + ov                            # Reflect vector direction.

        # Create new ray.
        _, p = super().intersect(ray)
        p2 = np.add(p, np.multiply(rd, 1e-5))   # Move the origin of ray slightly forward.
        r_ray = Ray(p2, rd)                     # Reflect ray.

        # print(ray.direction(), " : ", rd)
        c = tuple(np.multiply(r_ray.color(objects), 0.8).astype(int))
        return c

