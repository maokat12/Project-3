from time import *
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.motor import Motor

#FUNCTION FOR BIN IDENTIFICATIION
def bin_identify(time):
	#use lambda function?
		#linear function to determine where on the scale time lies
		#you'll have to do math here
		
	bin_weight = lambda time: 5*time #to be changed
	
	if bin_weight < 80 #
		bin_type = 'organic'
		print('Bin Type: organic')
	elif bin_weight >= 80 and bin_weight < 110
		bin_type = 'ceramic'
		print('Bin Type: ceramic')
	else	
		bin_type = 'metallic'
		print('Bin Type: metallic')
		
	return bin_type

#CHECK NUMBERS -> tacho distance, power
def lift_bin(touch_sensor, motor_arm):
	initial_pos = motor_arm.get_tacho()
	max_distance = 15 #number to be changed
	power = 50 #number to be changed
	time = []
	
	while get_tacho() - initial_pos <= max_distance 
		motor_arm.run(power = power)
		if touch_sensor.is_pressed() == FALSE:
			time.append(time())
			
	motor_arm.idle()
	stop = time()
	total_time = stop - time[0]
	print(total_time)
	
	return total_time
	
#TO DO	
def travel_to(bin_type):
	if bin_type == 'organic':
		#robot travels to organic bin drop off
	
	elif bin_type == 'ceramic'
		#robot travels to ceramic bin drop off
	
	elif bin_type == 'metallic'
		#robot travles to metallic bin drop off
	