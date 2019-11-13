import numpy as np
import math

class Ray():
    def __init__(self, origin, direction):
        self._origin = origin
        self._direction = direction / np.linalg.norm(direction)

    def origin(self):
        return self._origin

    def direction(self):
        return self._direction

    def extension_point(self, t):
        return self._origin + np.multiply(self._direction, t)

    def move_origin(self, t):
        self._origin = self.extension_point(t)
        return self

    def color(self, objects):
        o = None
        t = 1e+5
        for o2 in objects:
            t2, _ = o2.intersect(self)
            if (t2 is not None) and (t2 < t):
                t = t2
                o = o2

        if o is None:
            return (0, 0, 0)

        return o.color(self)
