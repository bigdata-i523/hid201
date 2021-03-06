import grovepi
import time
import paho.mqtt.client as mqtt
from servo_robot import ServoRobot

def on_connect(client, user_data, flags, rc):
	if rc == 0:
		print "connection sucessful"
	else:
		print "error while cnnecting"

def on_log(client, user_data, level, buff):
	print "log : ", buff

def on_message(client, user_data, msg):
	s = msg.payload
	t = 0.01
	if s == "F":
		robot.move_forward(t)
	elif s == "B":
		robot.move_backward(t)
	elif s == "L":
		robot.turn_left(t)
	elif s == "R":
		robot.turn_right(t)
	else:
		print "INVALID MESSAGE"

client = mqtt.Client("robot")
client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log

robot = ServoRobot(left_wheel = 3, right_wheel = 5)

client.connect('10.42.0.1')
client.subscribe('topic/control')
client.loop_forever()
