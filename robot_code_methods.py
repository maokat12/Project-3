import time
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.motor import Motor

###############################################################################
## Notes
###############################################################################
#MotorA -> (+) - lift arm up
#       -> (-) - lower arm

#Low Power
#power1 = 64.95
#power2 = 69
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
                motor_arm.brake()
                bin_type = 'metallic'
            else:
                motor_arm.brake()
                bin_type = 'ceramic'
        else:
            motor_arm.brake()
            bin_type = 'organic'
                
    motor_arm.brake()
    return(bin_type)
	
#TO DO	
'''def travel_to(bin_type):
	if bin_type == 'organic':
		#robot travels to organic bin drop off
	elif bin_type == 'ceramic'
		#robot travels to ceramic bin drop off
	elif bin_type == 'metallic'
		#robot travles to metallic bin drop off'''
	
