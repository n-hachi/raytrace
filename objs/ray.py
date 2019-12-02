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

    def intersect(self, objects):
        o = None
        t = 1e+10   # Large value
        p = None

        for o2 in objects:
            t2, p2 = o2.intersect(self)
            if t2 is None:
                continue
            if t2 < t:
                o = o2
                t = t2
                p = p2

        return o, t, p

    def color(self, objects, lights):
        o, t, _ = self.intersect(objects)

        if o is not None:
            return o.color(self, objects, lights)

        return np.array([64, 64, 64])
