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
