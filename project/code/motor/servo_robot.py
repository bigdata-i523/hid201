import time
from continuous_servo import ContinuousServo


class ServoRobot:
	def __init__(self, left_wheel, right_wheel):
		"""
		initialise the servo for whels
		"""
		self.left = ContinuousServo(left_wheel)
		self.right = ContinuousServo(right_wheel)

	def move_forward(self, t = 1):
		"""
		move the robot forward for t seconds
		turn both motors forward
		"""
		self.left.forward()
		self.right.forward()
		time.sleep(t)
		self.stop()

	def move_backward(self, t = 1):
		"""
		move the robot backward for t seconds
		turn both motors backwards
		"""

		self.left.backward()
		self.right.backward()
		time.sleep(t)
		self.stop_back()

	def turn_right(self, t = 1):
		"""
		turn right for t seconds
		turn the left wheel forward
		"""
		self.left.forward()
		time.sleep(t)
		self.stop()


	def turn_left(self, t = 1):
		"""
		turn left for t seconds
		turn the right wheel forward
		"""
		self.right.forward()
		time.sleep(t)
		self.stop()

	def stop(self):
		"""
		stop moving
		stop both motors
		"""
		self.left.stop()
		self.right.stop()

	def stop_back(self):
		"""
		stop moving
		stop both motors
		"""
		self.left.stop_back()
		self.right.stop_back()



if __name__ == "__main__":
	robot = ServoRobot(3,5)

	print "lft"
	robot.turn_left(2)
	print "rt"
	robot.turn_right(2)
