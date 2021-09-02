#/darkplaces

import rhinoscriptsyntax as rs
import random
import math

z =-100
radius = 0
theta = 0

count = 0
while z <= 100:
	if count % 2 ==0:
		x = (radius + 2) * math.cos(theta)
		y = (radius + 2) * math.sin(theta)
	else:
		x = radius * math.cos(theta)
		y = radius * math.sin(theta)
	
	rs.AddPoint((x,y,z))

	radius += .005
	theta += 2
	z = z + .05
	count += 1
