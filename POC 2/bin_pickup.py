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
## Notes
###############################################################################
#MotorA -> (+) - lift arm up
#       -> (-) - lower arm
#MotorB -> (+) - drive forward
# 		-> (-) - drive backwards

#Low Power
#B/C foward run power = 80
#B/C backward run power = 90
#A lower arm power - -70
#power2 = 69

###############################################################################
## Action
###############################################################################

while True:
    dist = float(ultrasonic.get_distance())/256
    print(dist)
    
    if dist <= 0.029:
        motorB.run(power = 0)
        motorC.run(power = 0)
        
        print(lift_identify(motorA))
        time.sleep(1)
        
        motorB.run(power = 80)
        motorC.run(power = 80)
        time.sleep(3)
        
        motorB.brake()
        motorC.brake()
        
        motorA.run(-70)
        time.sleep(1)
        motorA.idle()
        
        motorB.run(-90)
        motorC.run(-90)
        time.sleep(5)
        
        motorB.brake()
        motorC.brake()        
        
        break
		
    elif dist > 0.029: #low speed
		motorB.run(power = 80)
		motorC.run(power = 80)
