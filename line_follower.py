#!/usr/bin/env python

from time import *
import nxt.locator
from nxt.motor import *
from nxt.sensor import *

WHITE = 300
BLACK = 600
THRESHOLD = 50
TIME_LIMIT = 10

global left_light
global right_light
global left_motor
global right_motor
global brick

def setup():
  global left_light, right_light, left_motor, right_motor
  left_light = Light(brick, PORT_1)
  right_light = Light(brick, PORT_2)
  left_motor = Motor(brick, PORT_B)
  right_motor = Motor(brick, PORT_C)

def go(speed):
  global left_motor, right_motor
  left_motor.run(speed)
  right_motor.run(speed)

def stop():
  left_motor.brake()
  right_motor.brake()

def get_light():
  global left_motor, right_motor
  left_light.set_illuminated(True)
  right_light.set_illuminated(True)
  print 'Light: ', left_light.get_sample()
  print 'Light: ', right_light.get_sample()
  right_light.set_illuminated(False)
  left_light.set_illuminated(False)

def pathfind():
  global left_motor, right_motor

  start = time()
  go(40)

  while time() - start < TIME_LIMIT:
    print time()-start

    if left_light.get_sample() < 35:
      right_motor.turn(50, 22)
    elif right_light.get_sample() < 52:
      left_motor.turn(50, 22)
  stop()


# For USB
brick = nxt.locator.find_one_brick(name = 'NXT')

# For Bluetooth
#brick = nxt.bluesock.BlueSock('00:16:53:16:E6:34').connect()

setup()
get_light()
pathfind()

exit()
