import nxt
import nxtConnect # has to be in search path
from nxt.sensor import Ultrasonic, PORT_4
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C

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
    
#########################################################
import time

#ultraSonic = Ultrasonic(brick, PORT_4) #ultrasonic sensor
motorB = Motor(brick, PORT_C) #Right motor
motorC = Motor(brick, PORT_B) #Left motor

#def ultra(sensor):
	#return sensor.get_distance()

#distance = ultra(ultraSonic)

'''while(distance > 100):
    motorR.run(power = -70)
    motorL.run(power = -70)
    sleep(2)
    distance = ultra(ultraSonic)

Motor(brick, PORT_C).idle()
Motor(brick, PORT_B).idle()'''

while True:
    motorB.run(power = 50)
    motorA.run(power = 50)
	

