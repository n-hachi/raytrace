from abc import ABCMeta, abstractmethod
import numpy as np

from .ray import Ray

class AbsObject(metaclass=ABCMeta):

    @abstractmethod
    def normal(self, ray):
        raise NotImplementedError()

    @abstractmethod
    def reflect(self, ray):
        raise NotImplementedError()

    @abstractmethod
    def intersect(self, ray):
        raise NotImplementedError()

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
    def reflect(self, ray):
        n = self.normal(ray)
        cos = np.dot(ray.direction(), n.direction()) * -1   # Cosine
        rn = np.multiply(n.direction(), cos)                # Resize normal

        ov = np.add(ray.direction(), rn)        # Vector between origin ray and normal ray.
        rd = rn + ov                            # Reflect vector direction.

        # Create new ray.
        _, p = self.intersect(ray)
        p2 = np.add(p, np.multiply(rd, 1e-5))   # Move the origin of ray slightly forward.
        return Ray(p2, rd)                      # Reflect ray.

    def color(self, ray, objects, lights):
        r = self.reflect(ray)
        n = self.normal(ray)

        diffues = 0
        specular = 0
        # Generate ray between intersect point and light source.
        for l in lights:
            # Ray to light source
            r2l = Ray(r.origin(), l.center() - r.origin())
            o, _, _ = r2l.intersect(objects)

            if o is not None:
                continue

            diffues += max(0, np.dot(r2l.direction(), n.direction()))
            specular += max(0, np.dot(r2l.direction(), r.direction())) ** 50 * l.intensity()

        coefficient = (diffues + specular) / 2
        return np.multiply(self._surface_color, coefficient)
