#!/usr/bin/env python

import nxt.locator
from nxt.motor import *

b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_C)
m_left.turn(50, 25) # power, degrees
