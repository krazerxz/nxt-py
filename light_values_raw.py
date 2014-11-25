#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
from time import *

global left_light
global right_light
global brick

def setup():
  global left_light, right_light
  right_light = Light(brick, PORT_2)
  left_light = Light(brick, PORT_3)
  left_light.set_illuminated(True)
  right_light.set_illuminated(True)

def print_light_values():
  global left_light, right_light
  print 'Left: ', left_light.get_sample()
  print 'Right: ', right_light.get_sample()
  print '------------------'


brick = nxt.locator.find_one_brick(name = 'NXT')

setup()

while True:
  sleep(0.5)
  print_light_values()

exit()
