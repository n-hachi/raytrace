from abc import ABCMeta, abstractmethod
import numpy as np

from .objs import AbsObject
from .ray import Ray

class AbsPlane(AbsObject):

    def __init__(self, normal):
        self._normal = normal

    def normal(self, ray):
        _, p = self.intersect(ray)

        if p is None:
            return None

        return Ray(p, self._normal)


