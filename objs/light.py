class Light():
    def __init__(self, center, intensity):
        self._center = center
        self._intensity = intensity

    def center(self):
        return self._center

    def intensity(self):
        return self._intensity
