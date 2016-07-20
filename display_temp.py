#!/usr/bin/python -u

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
from Adafruit_LED_Backpack import AlphaNum4

display = AlphaNum4.AlphaNum4()
display.begin()

def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)

display.clear()
display.write_display()

def write_display(text):
    display.print_str(text)
    display.write_display()


print 'Press Ctrl-C to quit.'
while True:
    temp = sensor.readTempC()
    display.clear()
    temp_in_f = int(c_to_f(temp))
    write_display("{} F".format(temp_in_f))
    time.sleep(5)
    write_display("{} C".format(int(temp)))
    time.sleep(5)
