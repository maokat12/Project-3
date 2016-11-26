import time
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.motor import Motor

###############################################################################
## Notes
###############################################################################
#MotorA -> (+) - lift arm up
#       -> (-) - lower arm

#Low Battery
#power1 = 64.95
#power2 = 69

#High Battery
#power1 = 
#power2 = 
###############################################################################
## Action
###############################################################################

#Lift bin and identify the bin type
def lift_identify(motor_arm):
    max_distance = 65
    power1 = 64.95
    power2 = 69
    
    initial_pos = int(motor_arm.get_tacho().block_tacho_count)   #based garrett
    
    while int(motor_arm.get_tacho().block_tacho_count) - initial_pos <= max_distance:
        motor_arm.run(power = power1)
        time.sleep(.8)
        if int(motor_arm.get_tacho().block_tacho_count) - initial_pos < max_distance:
            motor_arm.run(power = power2)
            time.sleep(.3)
            if int(motor_arm.get_tacho().block_tacho_count) - initial_pos <= max_distance:
                while int(motor_arm.get_tacho().block_tacho_count) - initial_pos <= max_distance:
					motor_arm.run(power = power2+2)
				motor_arm.brake()
                bin_type = 'metallic'
            else:
                motor_arm.brake()
                bin_type = 'ceramic'
        else:
            motor_arm.brake()
            bin_type = 'organic'
                
    motor_arm.idle()
    return(bin_type)
	
def line_follow(motorB, motorC, light):
	light_val = light.get_sample()  #Numbers to be checked/changed
	if light_val > 40:
		#robot drives forward
		motorB.run(power = 60)
		motorC.run(power = 60)
	else:
		while(light val <= 40)
			#robot turns left for 2 seconds
			motorB.run(power = -50)
			motorC.run(power = 50)
			time.sleep(2)
			#robot turns right until it find a line
			motorB.run(power = 50)
			motorC.run(power = -50)