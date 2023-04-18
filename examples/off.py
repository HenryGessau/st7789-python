#!/usr/bin/env python3
import sys

import ST7789 as ST7789

print("""
off.py - turn the display off
""")

if len(sys.argv) > 1:
    print("Usage: {}\n".format(sys.argv[0]))
    sys.exit(1)

disp = ST7789.ST7789(
    height=240,
    rotation=90,
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=0,
    offset_top=0
)

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

print('Turning off ...')

disp.set_backlight(0)
