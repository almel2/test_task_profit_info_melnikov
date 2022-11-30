import numpy as np
from PIL import Image, ImageDraw

img = Image.open('../images/1556708032_1.jpg', 'r')
arr = np.array(img)

img = img.resize((1000, 800))
width, height = img.size

print(img.format, img.size, img.mode)

luminance_max_dark = 255 ** 10000
coordinates_max_dark = [0, 0]

luminance_max_light = 0
coordinates_max_light = [0, 0]

for x in range(height - 100):
    for y in range(width - 100):
        rgb_area_100_x_100 = arr[x:x + 101, y:y + 101]
        luminance = np.sum(rgb_area_100_x_100) / 255

        if luminance < luminance_max_dark:
            luminance_max_dark = luminance
            coordinates_max_dark[0] = x
            coordinates_max_dark[1] = y

        if luminance > luminance_max_light:
            luminance_max_light = luminance
            coordinates_max_light[0] = x
            coordinates_max_light[1] = y

draw = ImageDraw.Draw(img)
draw.rectangle((coordinates_max_dark[0],
                coordinates_max_dark[1],
                (coordinates_max_dark[0] + 100),
                (coordinates_max_dark[1] + 100)),
               outline=(255, 255, 255))
draw.rectangle((coordinates_max_light[0],
                coordinates_max_light[1],
                (coordinates_max_light[0] + 100),
                (coordinates_max_light[1] + 100)),
               outline=(0, 255, 0))

img.show()

print(luminance_max_dark)
print(coordinates_max_dark)

print(luminance_max_light)
print(coordinates_max_light)
