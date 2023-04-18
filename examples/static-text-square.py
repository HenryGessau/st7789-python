#!/usr/bin/env python3
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789

MESSAGE = "Hello World! How are you today?"

try:
    MESSAGE = sys.argv[1]
except IndexError:
    print("""Usage: {} "<message>" """.format(sys.argv[0]))
    exit(1)

# Create ST7789 LCD display class.

disp = ST7789.ST7789(
    height=240,
    rotation=90,
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,  # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=0,
    offset_top=0
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

draw.rectangle((0, 0, WIDTH, HEIGHT), (0, 0, 0))
draw.multiline_text((5, 3), MESSAGE, fill=(255, 255, 255), font=font, align="center")
disp.display(img)
