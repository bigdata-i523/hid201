from stepper_motor import StepperMotor
from threading import Thread
import time
import RPi.GPIO as GPIO

class StepperRobot:
	def __init__(self, left_pins = [7,11,13,15], right_pins = [8,10,12,16], delay=0.001, full_step = False):
		"""
		initialise the stepper motors
		delay  = delay for the motor
		full_step = False uses half stepping to turn the stepper motor
		"""
		self.left = StepperMotor(pins = left_pins, delay = delay, full_step = full_step)
		self.right = StepperMotor(pins = right_pins, delay = delay, full_step = full_step)

	def move_forward(self, step_count = 100):
		"""
		move the robot forward
		turn both motors forward
		"""
		t_1 = Thread(target= self.left.backward, args=(step_count,))
		t_2 = Thread(target= self.right.forward, args=(step_count,))
		t_1.start()
		t_2.start()

	def move_backward(self, step_count = 100):
		"""
		move the robot backward
		turn both motors backward
		"""
		t_1 = Thread(target= self.left.forward, args=(step_count,))
		t_2 = Thread(target= self.right.backward, args=(step_count,))
		t_1.start()
		t_2.start()

	def turn_right(self, step_count = 50):
		"""
		turn the robot right
		turn right motor backward
		turn left motor forward
		"""
		t_1 = Thread(target= self.left.backward, args=(step_count,))
		t_2 = Thread(target= self.right.backward, args=(step_count,))
		t_1.start()
		t_2.start()

	def turn_left(self, step_count = 50):
		"""
		turn the robot left
		turn right motor forward
		turn left motor backward
		"""
		t_1 = Thread(target= self.left.forward, args=(step_count,))
		t_2 = Thread(target= self.right.forward, args=(step_count,))
		t_1.start()
		t_2.start()


if __name__ == "__main__":
	r = StepperRobot()
	print "forward"
	r.move_forward()
	time.sleep(3)

	print "back"
	r.move_backward()
	time.sleep(3)

	print "left"
	r.turn_left(100)
	time.sleep(3)

	print "right"
	r.turn_right(100)
	time.sleep(3)

	GPIO.cleanup()


# TODO
# stepper_motor robot publisher --> set time delay
# otherwise the threads have conflicts
#
# use different pins for left as sda and clk are always on
# build and run
# connect wheels somehow

