import grovepi
import time


class ContinuousServo:
	def __init__(self, pin=3):
		"""
		initialize the servo
		"""
		self.servo = pin
		grovepi.pinMode(self.servo, 'OUTPUT')

	def forward(self):
		"""
		turn the motor forward indefinitely
		"""
		grovepi.analogWrite(self.servo, 1)

	def backward(self):
		"""
		turn the motor backward indefinitely
		"""
		grovepi.analogWrite(self.servo, 250)

	def stop(self):
		"""
		stop the motor seemlessly, when moving forward
		"""
		grovepi.analogWrite(self.servo, 0)

	def stop_back(self):
		"""
		stop the motor seemlessly when moving backward
		"""
		grovepi.analogWrite(self.servo, 255)

if __name__ == "__main__":
	servo = ContinuousServo(5)
	print "turn forward"
	servo.forward()
	time.sleep(2)

	print "stop"
	servo.stop()
	time.sleep(1)

	print "turn backward"
	servo.backward()
	time.sleep(2)

	print "stop"
	servo.stop()
	time.sleep(1)
