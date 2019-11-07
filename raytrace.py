import numpy as np
from PIL import Image
import math
import objs

HEIGHT = 480
WIDTH = 640
FOV = math.pi / 3.0
ORIGIN = np.array([0, 0, 0])

def main():
    sphere = objs.Sphere([0, 0, 4], 1)

    img = Image.new('RGB', (WIDTH, HEIGHT))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dir_x = (x + 0.5) - (WIDTH / 2)
            dir_y = (y + 0.5) - (HEIGHT / 2)
            dir_z = HEIGHT / (2 * math.tan(FOV / 2))
            ray = objs.Ray(ORIGIN, [dir_x, dir_y, dir_z])

            if sphere.intersect(ray):
                img.putpixel((x, y), (255, 255, 255))
            else:
                img.putpixel((x, y), (0, 0, 0))

    img.save('output.png')

if __name__ == '__main__':
    main()
