#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
from nxt.motor import *
from time import *

global left_light
global right_light
global left_calibrate
global right_calibrate
global left_motor
global right_motor
global arm_motor
global rgb_sensor
global brick

def setup():
  global left_light, right_light, left_calibrate, right_calibrate, left_motor, right_motor, rgb_sensor, arm_motor
  rgb_sensor = Color20(brick, PORT_1)
  right_light = Light(brick, PORT_2)
  left_light = Light(brick, PORT_3)
  left_calibrate = left_light.get_sample()
  right_calibrate = right_light.get_sample()
  left_motor = Motor(brick, PORT_B)
  right_motor = Motor(brick, PORT_A)
  arm_motor = Motor(brick, PORT_C)

def print_light_values():
  global left_calibrate, right_calibrate
  print 'Left: ', get_l_sample()
  print 'Right: ', get_r_sample()
  print 'Detected Colour: ', color_to_string(rgb_sensor.get_reflected_light(0x0D))
  print '------------------'

def color_to_string(color_int):
  if color_int == 2:
    return 'BLUE'
  elif color_int == 3:
    return 'GREEN'
  elif color_int == 5:
    return 'RED'
  else:
    return False

def is_color_detected():
  color = color_to_string(rgb_sensor.get_reflected_light(0x0D))
  if color != False:
    move_arm(color)

def move_arm(color):
  if (color == 'GREEN'):
    #Pick up
    arm_motor.turn(80, 30)
  elif (color == 'RED'):
    arm_motor.turn(-80, 30)
    #exit()

def get_l_sample():
  global left_calibrate, left_light
  return left_light.get_sample() - left_calibrate

def get_r_sample():
  global right_calibrate, right_light
  return right_light.get_sample() - right_calibrate

def sensor_difference():
  if get_l_sample() - get_r_sample() > 35:
    return 'LEFT'
  elif get_r_sample() - get_l_sample() > 35:
    return 'RIGHT'
  else:
    return False

def correct(direction):
  if direction == 'LEFT':
   left_motor.turn(90, 20)
   right_motor.turn(-90, 20)
   print 'LEFT'
  elif direction == 'RIGHT':
    right_motor.turn(90, 20)
    left_motor.turn(-90, 20)
    print 'RIGHT'

def go(speed):
  global left_motor, right_motor
  left_motor.run(speed)
  right_motor.run(speed)

def stop():
  left_motor.brake()
  right_motor.brake()

# For USB
brick = nxt.locator.find_one_brick(name = 'NXT')

setup()

left_light.set_illuminated(True)
right_light.set_illuminated(True)

while True:
  #sleep(0.5)
  #go(100)
  print_light_values()
  #while sensor_difference() != False:
    #stop()
    #correct(sensor_difference())
  is_color_detected()

right_light.set_illuminated(False)
left_light.set_illuminated(False)

exit()
