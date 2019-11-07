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
