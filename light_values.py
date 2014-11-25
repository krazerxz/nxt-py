#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
from time import *

global left_light
global right_light
global left_calibrate
global right_calibrate
global brick

def setup():
  global left_light, right_light, left_calibrate, right_calibrate
  right_light = Light(brick, PORT_2)
  left_light = Light(brick, PORT_3)
  left_light.set_illuminated(True)
  right_light.set_illuminated(True)
  left_calibrate = left_light.get_sample()
  right_calibrate = right_light.get_sample()

def print_light_values():
  print 'Left: ', get_l_sample()
  print 'Right: ', get_r_sample()
  print '------------------'

def get_l_sample():
  global left_calibrate, left_light
  return left_light.get_sample() - left_calibrate

def get_r_sample():
  global right_calibrate, right_light
  return right_light.get_sample() - right_calibrate

def sensor_difference():
  if get_l_sample() - get_r_sample() > 150:
    return 'LEFT'
  elif get_r_sample() - get_l_sample() > 150:
    return 'RIGHT'
  else:
    return False
brick = nxt.locator.find_one_brick(name = 'NXT')

setup()

while True:
  #sleep(0.5)
  print_light_values()
  while sensor_difference() != False:
    stop()

exit()
