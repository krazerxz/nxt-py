#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *

global brick
global rgb_sensor

def setup():
  global rgb_sensor
  rgb_sensor = Color20(brick, PORT_1)

def print_light_values():
  #rgb_sensor.set_light_color(")
  print 'Colour: ', rgb_sensor.get_reflected_light(0x0D)
  print '------------------'

# For USB
brick = nxt.locator.find_one_brick(name = 'NXT')

setup()

while True:
  print_light_values()


exit()
