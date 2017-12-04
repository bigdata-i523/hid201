from __future__ import print_function
import paho.mqtt.client as mqtt
import picamera
from picamera.array import PiRGBArray
import cv2
import time
import sys
import os

def on_connect(client, user_data, flags, rc):
	if rc == 0:
		print( "connected")
	else:
		print( "error while connecting")

def on_log(client, user_data, level, buff):
	print( "log :" + str( buff))



print("setting camera")
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 30
raw_capture = PiRGBArray(camera, size = (640,480))

#time.sleep(5)

client = mqtt.Client("Video")
client.on_connect = on_connect
#client.on_log = on_log


#client.connect('10.42.0.1')
if len(sys.argv) > 1:
	broker = sys.argv[1]
else:
	broker = '10.0.0.8'

path = os.getcwd()
if path.endswith('mqtt_video'):
	filename = path + '/faces.xml'
else:
	filename = path + '/mqtt_video/faces.xml'

client.connect(broker)
client.loop_start()

face_cascade = cv2.CascadeClassifier(filename)
#face_cascade.load('faces.xml')

for frame in camera.capture_continuous(raw_capture, format='bgr', use_video_port=True):
	image = raw_capture.array
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	try :
        	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
		for (x,y,w,h) in faces:
	    		cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
	except:
		print("some error")
	buff = bytearray(gray)
	client.publish('topic/video_frames', buff)
	raw_capture.truncate(0)
	time.sleep(0.1)

