from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic, 
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

# use try with finally to stop motors at end, even if
# program encountered a (programming) error

ultrasonic = Ultrasonic(brick, PORT_1)
motorA = Motor(brick, PORT_A) #arm
motorB = Motor(brick, PORT_B) #right
motorC = Motor(brick, PORT_C) #left

while True: 
	dist = float(ultrasonic.get_distance())/256
	print(dist)
	if dist < .06: #stop motors
		motorB.run(power = 0)
		motorC.run(power = 0)
	elif dist >= 0.2 and dist < 0.3: #low speed
		motorB.run(power = -65 - (5*dist))
		motorC.run(power = -65 - (5*dist))
	elif dist >= 0.06 and dist < 0.2: #medium speed
		motorB.run(power = -70 - (10 * dist))
		motorC.run(power = -70 - (10 * dist))
	else: #high speed
		motorC.run(power = -80 - (10 * dist))
		motorB.run(power = -80 - (10 * dist))
