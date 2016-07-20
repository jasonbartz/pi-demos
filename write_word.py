import sys
from Adafruit_LED_Backpack import AlphaNum4

display = AlphaNum4.AlphaNum4()

display.begin()

# Scroll a message across the display
message = sys.argv[1]
display.clear()
display.print_str(message)
display.write_display()
