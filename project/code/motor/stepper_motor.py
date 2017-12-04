import time
import RPi.GPIO as GPIO

class StepperMotor:
	def __init__(self, pins = [3,5,7,11], delay = 0.001, full_step = False):
		"""
		initialise the GPIO pins for the motor
		full_step = true uses full stepping technique
		default is half stepping
		full stepping gives more torque but is not as smooth
		using half stepping effictive torque = 70% of full stepping
		increasing the delay reduces the speed of the motor
		"""
		self.pins = pins
		self.delay = delay
		GPIO.setmode(GPIO.BOARD)

		for pin in self.pins:
			GPIO.setup(pin, GPIO.OUT)

		if not full_step:
			self.steps = [[0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], [0,1,0,0], [1,1,0,0], [1,0,0,0], [1,0,0,1]]
		else:
			self.steps = [[0,0,1,1], [0,1,1,0], [1,1,0,0], [1,0,0,1]]

		self.reverse_steps = [self.steps[i] for i in range(len(self.steps) - 1, -1, -1)]

	def set_step(self, step = [0,0,0,0]):

		GPIO.setmode(GPIO.BOARD)
		for i in range(4):
			GPIO.output(self.pins[i], step[i])

	def forward(self, step_count = 100):
		"""
		turn the motor forward for 100 counts
		step_count = 512 for a full rotation
		default = 100
		"""
		for i in range(step_count):
			for step in  self.reverse_steps:
				self.set_step(step)
				time.sleep(self.delay)

	def backward(self, step_count = 100):
		"""
		turn the motor backwardfor 100 counts
		step_count = 512 for a full rotation
		default = 100
		"""

		for i in range(step_count):
			for step in self.steps:
				self.set_step(step)
				time.sleep(self.delay)


if __name__ == "__main__":
	pins = [3,5,7,11]
	stepper = StepperMotor(pins, delay = 0.001)

	print "turn one full rotation forward"
	stepper.forward(step_count = 20)
	"""
	time.sleep(1)

	print "turn one full rotation backward"
	stepper.backward(step_count = 512)
	time.sleep(1)

	print "turn one full rotation forward"
	stepper.forward(step_count = 512)
	time.sleep(1)
	"""
	GPIO.cleanup()
