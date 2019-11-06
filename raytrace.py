from PIL import Image

HEIGHT = 480
WIDTH = 640

def main():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = (int(x * 255 / WIDTH), int(y * 255 / HEIGHT), 0)
            img.putpixel((x, y), color)

    img.save('output.png')

if __name__ == '__main__':
    main()
