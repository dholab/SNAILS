#!/usr/bin/env python

# this modules are necessary to run the raspberry pi and interact with the general purpose input/output (GPIO) pins
import RPi.GPIO as GPIO
# this module is important for setting duration and pauses in the code
import time

# Set up pins
MotorPin1   = 17
MotorPin2   = 18
MotorEnable = 27

# this is the message that will print when the program is run and gives instructions to the user
def print_message():
	print ("========================================")
	print ("|                RAP pipette           |")
	print ("|    ------------------------------    |")
	print ("|     Motor pin 1 connect to GPIO0     |")
	print ("|     Motor pin 2 connect to GPIO1     |")
	print ("|     Motor enable connect to GPIO2    |")
	print ("|                                      |")
	print ("|         Controlling a motor          |")
	print ("|                                      |")
	print ("|                          O'Connor Lab|")
	print ("========================================\n")
	print ('Program is running...')
	print ('Please press Ctrl+C to end the program...')
	raw_input ("Press Enter to begin\n") # this is a built-in python function that receives input from the user

def setup():
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	# Set pins to output
	GPIO.setup(MotorPin1, GPIO.OUT)
	GPIO.setup(MotorPin2, GPIO.OUT)
	GPIO.setup(MotorEnable, GPIO.OUT, initial=GPIO.LOW) # sets the motor to off at the start

# Define a motor function to spin the motor
# direction should be 
# 1(clockwise), 0(stop), -1(counterclockwise)
# if the wires ever get switched, clockwise will become counterclockwise and vise versa
def motor(direction):
	# Clockwise
	if direction == 1:
		# Set direction
		GPIO.output(MotorPin1, GPIO.HIGH)
		GPIO.output(MotorPin2, GPIO.LOW)
		# Enable the motor
		GPIO.output(MotorEnable, GPIO.HIGH)
		print ("Clockwise")
	# Counterclockwise
	if direction == -1:
		# Set direction
		GPIO.output(MotorPin1, GPIO.LOW)
		GPIO.output(MotorPin2, GPIO.HIGH)
		# Enable the motor
		GPIO.output(MotorEnable, GPIO.HIGH)
		print ("Counterclockwise")
	# Stop
	if direction == 0:
		# Disable the motor
		GPIO.output(MotorEnable, GPIO.LOW)
		print ("Stop")

def main():
	print_message() # prints the message written above

	# Define a dictionary to make the script more readable
	# CW as clockwise, CCW as counterclockwise, STOP as stop
	directions = {'CW': 1, 'CCW': -1, 'STOP': 0}
	iteration = 1
	while iteration < 6:

		if iteration < 6:
			# Clockwise
			motor(directions['CW'])
			time.sleep(190)
			# Stop
			motor(directions['STOP'])
			time.sleep(30)
			# Counterclockwise
			motor(directions['CCW'])
			time.sleep(190)
			# Stop
			motor(directions['STOP'])
			time.sleep(30)
			print ("cycle: " +  str(iteration))
			iteration = iteration + 1
		else:
			print ("Error")

# stops the motor and unassigns the GPIO pins
def destroy():
	# Stop the motor
	GPIO.output(MotorEnable, GPIO.LOW)
	# Release resource
	GPIO.cleanup()    

# If trying to running this script directly, do:
if __name__ == '__main__':
	setup()
	try:
		main()
		print ("RAP Mix Completed")
	# When 'Ctrl+C' is pressed, the child program destroy() will be execut
	except KeyboardInterrupt:
		destroy()