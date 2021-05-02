import time
import board
import busio
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 14 segment 4 character display:
display = segments.Seg14x4(i2c)

# Clear the display.
display.fill(0)

# set brightness, range 0-1.0, 1.0 max brightness
display.brightness = 0.1

display.print("0000")