#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
from time import *

global left_light
global right_light
def setup():
  global left_light, right_light
  right_light = Light(brick, PORT_2)
  left_light = Light(brick, PORT_3)

brick = nxt.locator.find_one_brick(name = 'NXT')

setup()

while True:
  left_light.set_illuminated(True)
  right_light.set_illuminated(True)
  sleep(0.1)
  left_light.set_illuminated(False)
  right_light.set_illuminated(False)
  sleep(0.1)

exit()
