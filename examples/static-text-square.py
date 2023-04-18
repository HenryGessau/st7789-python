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
draw.rectangle((0, 0, WIDTH, HEIGHT), (0, 0, 0))

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
_, _, x, y = draw.multiline_textbbox((0, 0), MESSAGE, font=font, align="center")
if x > WIDTH or y > HEIGHT:
    print(f"Message too big for display! ({x}x{y} > {WIDTH}x{HEIGHT})")
    exit(1)

x = (WIDTH - x) // 2
y = (HEIGHT - y) // 2

draw.multiline_text((x, y), MESSAGE, fill=(215, 215, 215), font=font, align="center")
disp.display(img)
