###############################################################################
## First you need to connect to your NXT
###############################################################################

import nxt
import nxtConnect # has to be in search path

brickName = "MINI-14"
useUSB = False

if useUSB:
    brick = nxt.find_one_brick(
        name = brickName,
        strict = True,
        method = nxt.locator.Method(usb = True, bluetooth = True))
else:
    # the bluetooth function of the nxt library works too, but "wastes"
    # time searching for devices.
    brick = nxtConnect.btConnect(brickName)
    
print(brick.get_device_info()) # check what brick you connected to

###############################################################################
## Set-Up
###############################################################################

from robot_code_methods import *
from time import *
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic, 
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

# use try with finally to stop motors at end, even if
# program encountered a (programming) error

#sensors
ultrasonic = Ultrasonic(brick, PORT_4)
light = Light(brick, PORT_3)
touch = Touch(brick, PORT_1)
#compass = Compass(brick, PORT_2)

motorA = Motor(brick, PORT_A) #arm
motorB = Motor(brick, PORT_B) #right
motorC = Motor(brick, PORT_C) #left

###############################################################################
## Action
###############################################################################

while True: 
	dist = float(ultrasonic.get_distance())/256
	print(dist)
	
	if dist < .06: #stop motors
		motorB.run(power = 0)
		motorC.run(power = 0)
		
		time = lift_bin(motorA, touch)  #pick up bin
		sleep(10)  #wait
		
		motorB.run(power = 20)   #move a little bit
		motorC.run(power = 20)
		sleep(5)  #wait
		
		while(touch.is_pressed == FALSE)  #sets bin b
			motorA.run(power = -20)
		
	elif dist >= 0.2 and dist < 0.3: #low speed
		motorB.run(power = -65 - (5*dist))
		motorC.run(power = -65 - (5*dist))
	elif dist >= 0.06 and dist < 0.2: #medium speed
		motorB.run(power = -70 - (10 * dist))
		motorC.run(power = -70 - (10 * dist))
	else: #high speed
		motorC.run(power = -80 - (10 * dist))
		motorB.run(power = -80 - (10 * dist))