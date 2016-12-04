import time
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor.hitechnic import Compass
from nxt.motor import Motor

###############################################################################
## Notes
###############################################################################
#MotorA -> (+) - lift arm up
#       -> (-) - lower arm
#MotorB -> (+) - drive forward
# 		-> (-) - drive backwards
#
#motorB -> right
#motorC -> left
#
#right, 1 power value lower than left
#
#Compass
#       -> (N) - 0
#       -> (E) - 90
#       -> (S) - 180
#       -> (W) - 270
#
#Low Power
#power1 = 64.95
#power2 = 69
#
#High Power 
#power1 = 63
#power2 = 67
#
#Bright Lighting - 350
#Low Lighting - 300
#
###############################################################################
## Action
###############################################################################

#Lift bin and identify the bin type
def lift_identify(motor_arm):
    max_distance = 65
    power1 = 63
    power2 = 67
    
    initial_pos = int(motor_arm.get_tacho().block_tacho_count)   #based garrett
    
    while int(motor_arm.get_tacho().block_tacho_count) - initial_pos <= max_distance:
        motor_arm.run(power = power1)
        time.sleep(1)
        if int(motor_arm.get_tacho().block_tacho_count) - initial_pos < max_distance:
            motor_arm.run(power = power2)
            time.sleep(1)
            if int(motor_arm.get_tacho().block_tacho_count) - initial_pos <= max_distance:
                motor_arm.run(power = power2+2)
                motor_arm.idle()
                bin_type = 'metallic'
                break
            else:
                motor_arm.idle()
                bin_type = 'ceramic'
                break
        else:
            motor_arm.idle()
            bin_type = 'organic'
            break
                
    motor_arm.brake()
    return(bin_type)
    
def line_follow(motorB, motorC, light):
    
    light_val = light.get_sample()
    lightness = 400 #CALIBRATE BEFORE RUNNING
    
    if light_val < lightness:  
        motorB.run(power = 80)
        motorC.run(power = 80)
        
    elif light_val >= lightness:
        initial_pos = int(motorB.get_tacho().block_tacho_count)
        #turn right for a set distance
        while int(motorB.get_tacho().block_tacho_count) - initial_pos <= 800: 
            motorB.run(power = 80)
            motorC.run(power = -80)
            light_val = light.get_sample()
            if light_val < lightness:
                motorB.run(power = 80)
                motorC.run(power = 80)
                time.sleep(.5)
                break
		
	#turn left for a set distance
	while int(motorC.get_tacho().block_tacho_count) - initial_pos <= 1600: 
            motorB.run(power = -80)
            motorC.run(power = 80)
            light_val = light.get_sample()
            if light_val < lightness:
                motorB.run(power = 80)
                motorC.run(power = 80)
                time.sleep(.5)
                break
		
	#turn turn back to original position
        while int(motorB.get_tacho().block_tacho_count) - initial_pos <= 800: 
            motorB.run(power = 80)
            motorC.run(power = -80)
            light_val = light.get_sample()
            if light_val < lightness:
                motorB.run(power = 80)
                motorC.run(power = 80)
                time.sleep(.5)
                break
		
        #turn moves forwar til it finds a line
        while light_val > lightness:
            motorB.run(power = 80)
            motorC.run(power = 80)
            light_val = light.get_sample()

def fix_compass(reading)
	if reading > 180:
		reading = 360 - reading
		
	return reading
			
def drop_bin(motorB, motorC, motorA, touch, compass):
    
    #force angle to between 0 and 180
    initial_dir = compass.get_heading()
    initial_dir = fix_compass(initial_dir)
	
    current_dir = compass.get_heading()
    current_dir = fix_compass(current_dir)
	
    #turn ~90 degrees    
    while current_dir - initial_dir != 90:
        motorC.run(power = -80)
        motorB.run(power = 80)
        current_dir = compass.get_heading()
        current_dir = fix_compass(current_dir)
        
    #move forward a set amount
    initial_pos = int(motorB.get_tacho().block_tacho_count)
    while int(motorB.get_tacho().block_tacho_count) - initial_pos <= 200: #maybe change distance?
        motorC.run(power = 80)
        motorB.run(power = 80)
        
    #set down bin
    while touch.is_pressed() is False:
        motorA.run(power = -70)
       
    #move backwards a set amount    
    while abs(int(motorB.get_tacho().block_tacho_count) - initial_pos) > 5: #arbitrary number, needs testing
        motorC.run(power = -80)
        motorB.run(power = -80)
    
    #turn back 90 degrees
    while abs(current_dir - intial_dir) > 10:
        motorC.run(power = -80)
        motorB.run(power = 80)
        current_dir = compass.get_heading()
        current_dir = fix_compass(current_dir)
