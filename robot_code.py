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

#######################################################################
## Then, you can specify what you want the NXT to do
#######################################################################

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

light.set_illuminated(TRUE)
have_bin = TRUE #have bin true or false


#USE FUNCTIIONSSSSSSSSSS

#process
#does not have bin
#check if there's a bin
	#get bin distance
		#if bin close enough -> prepare to pick up bin
	#pick up bin
#see where you are on line
	#PID control	
	#turn left/right to fix
	#move forward x steps?
#repeat til bin is found

#has bin
#determine type of bin
	#display in screen
	#make noise
		#1 pip - ceramic
		#2 pips - metallic
		#3 pips - organic
#look for marker
	#type of marker for each has to be hardcoded --> FIGURE THIS OUT
#travel to correct marker
#identify correc place to drop bin off
#drop bin off
#step away from bin without knocking it over


	

while True:
	light_value = light.get_lightness()    #test this to see what values this returns
	distance = ultrassonic.get_distance() / 256   #0 < distance < 256 -> raw values -> fixed
	
	#PID Method -> follow edge of line, not middle
	#figure out which side of the line following -> inside vs outside
	if(light_value < 0.5 and light_value < 0.4): #numbers subject to change
		motorB.run(power = 50)  #-127 > power > 128 I think???//
		motorC.run(power = 50)  #check this^
	elif():
		
		
		
		
#pick up bin
