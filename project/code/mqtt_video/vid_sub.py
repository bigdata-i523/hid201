import paho.mqtt.client as mqtt
import time
import cv2
import numpy as np
import sys

def on_connect(client, use_data, flags, rc):
	if rc == 0:
		print "connected"
		client.subscribe('topic/video_frames')
	else:
		print "error"

def on_log(client, user_data, level, buff):
	print "log :",buff

def on_message(client, user_data, msg):
	buff = msg.payload
	#print "buff :", buff
	# read np arry from string
	image = np.fromstring(buff,np.uint8).reshape(480, 640, 1) #maybe use cv2.imdecode
	cv2.imshow('image', image)
	cv2.waitKey(10)

client = mqtt.Client('Video_sub')
client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log

if len(sys.argv) >1:
	broker = sys.argv[1]
else:
	broker = '127.0.0.1'

client.connect(broker)
client.loop_forever()
