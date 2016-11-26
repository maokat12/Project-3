#######################################################################
## First you need to connect to your NXT
#######################################################################

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
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

# use try with finally to stop motors at end, even if
# program encountered a (programming) error

#sensors
ultrasonic = Ultrasonic(brick, PORT_4)
light = Light(brick, PORT_3)
compass = Compass(brick, PORT_2)
touch = Touch(brick, PORT_1)

#motors
motorA = Motor(brick, PORT_A) #arm
motorB = Motor(brick, PORT_B) #right
motorC = Motor(brick, PORT_C) #left

light.set_illuminated(TRUE)
has_bin = False #have bin true or false

###############################################################################
## Notes
###############################################################################
#MotorA -> (+) - lift arm up
#       -> (-) - lower arm
#MotorB -> (+) - drive forward
# 		-> (-) - drive backwards

#USE FUNCTIIONSSSSSSSSSS

#process
#does not have bin
#check if there's a bin
	#get bin distance
		#if bin close enough -> prepare to pick up bin
	#pick up bin
#see where you are on line
	#PID control	
		#maybe not the best idea with dots/breaks in the line
	#follow edge or follow center of line
	#turn left/right to fix
	#move forward x steps?
#repeat til bin is found

#has bin
#determine type of bin
	#display in screen
		#1 pip - ceramic
		#2 pips - metallic
		#3 pips - organic
#look for marker
	#type of marker for each has to be hardcoded --> FIGURE THIS OUT
	#could use magnets instead
#travel to correct marker
#identify correc place to drop bin off
#drop bin off
#step away from bin without knocking it over

#numbers
#0 < distance < 256 -> raw values -> fixed
#-127 > power > 128 I think???//

###############################################################################
## Action
###############################################################################
	
while True:
	if has_bin is False:
		#robot moves around and looks for a bin
		dist = float(ultrasonic.get_distance())/256
		while(dist > 0.029):
			line_follow(motorB, motorC, light)
		bin_type = lift_identify(motorA)
		has_bin = True
		
	else:
		#robot looks for correct drop off point
		dist = float(ultrasonic.get_distance())/256
		if bin_type == 'metallic':
			color = 50 #number for light for color paper - blue?
		if bin_type == 'organic':
			color = 40 #orange?
		if bin_type == 'ceramic':
			color = 30 #red?
			
		light_val = light.get_sample()
		
		while light_val not color:
			line_follow(motorB, motorC, light)
		
		#robot drops off bin
		while touch.is_pressed is False:
			motorA.run(power = -50)
		
		has_bin = False

	
		
