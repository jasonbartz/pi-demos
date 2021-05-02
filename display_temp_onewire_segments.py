#!/usr/bin/python -u

import time
import os
import glob
import board
import busio
from adafruit_ht16k33 import segments

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
# Grabs the first probe out of the directory
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

display = segments.Seg14x4(i2c)



def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        return float(temp_string) / 1000.0


def write_display(text):
    # Clear the display.
    display.fill(0)

    # set brightness, range 0-1.0, 1.0 max brightness
    display.brightness = 1

    display.print(text)

print 'Press Ctrl-C to quit.'
while True:
    temp = read_temp()
    display.clear()
    temp_in_f = int(c_to_f(temp))
    write_display("{} F".format(temp_in_f))
    time.sleep(5)
    write_display("{} C".format(int(temp)))
    time.sleep(5)
