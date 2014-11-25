#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *

brick = nxt.locator.find_one_brick(name = 'NXT')
rgb_sensor = Color20(brick, PORT_1)
right_light = Light(brick, PORT_2)
left_light = Light(brick, PORT_3)

left_light.set_illuminated(False)
right_light.set_illuminated(False)
rgb_sensor.get_reflected_light(0x11)

exit()
