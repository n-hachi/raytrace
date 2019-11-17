import numpy as np
from PIL import Image
import math
import objs

HEIGHT = 480
WIDTH = 640
FOV = math.pi / 3.0
ORIGIN = np.array([0, 0, 0])

def main():
    objects = [
            objs.Sphere([-1, 0, 4], 1, (255, 0, 0)),
            objs.Circle([0, 4, 15], 8, [0, 1, 0], (0, 255, 0)),
            objs.Triangle([0, -1, 4], [6, -1, 8], [3, 2, 6], (0, 0, 255)),
            objs.CheckerdSphere([0, -2, 8], 2, (255, 255, 0)),
            ]

    img = Image.new('RGB', (WIDTH, HEIGHT))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dir_x = (x + 0.5) - (WIDTH / 2)
            dir_y = (y + 0.5) - (HEIGHT / 2)
            dir_z = HEIGHT / (2 * math.tan(FOV / 2))
            ray = objs.Ray(ORIGIN, [dir_x, dir_y, dir_z])
            img.putpixel((x, y), ray.color(objects))

    img.save('output.png')

if __name__ == '__main__':
    main()
