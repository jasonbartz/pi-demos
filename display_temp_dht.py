#!/usr/bin/python -u

import time

# import Adafruit_GPIO.SPI as SPI
# import Adafruit_MAX31855.MAX31855 as MAX31855
from Adafruit_LED_Backpack import AlphaNum4
import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT22
PIN = 4

display = AlphaNum4.AlphaNum4()
display.begin()


def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

display.clear()
display.write_display()


def write_display(text):
    display.print_str(text)
    display.write_display()


print 'Press Ctrl-C to quit.'
while True:
    display.clear()
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(c_to_f(temperature), humidity))
    write_display("{:0.0f}*".format(temperature))
    time.sleep(5)
    write_display("{:0.0f}%".format(humidity))
    time.sleep(5)
