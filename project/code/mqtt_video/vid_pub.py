import paho.mqtt.client as mqtt
import picamera
from picamera.array import PiRGBArray
import cv2
import time
import sys

def on_connect(client, user_data, flags, rc):
	if rc == 0:
		print "connected"
	else:
		print "error while connecting"

def on_log(client, user_data, level, buff):
	print "log :" , buff

print "setting camera"
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 30
raw_capture = PiRGBArray(camera, size = (640,480))

time.sleep(1)

client = mqtt.Client("Video")
client.on_connect = on_connect
#client.on_log = on_log


#client.connect('10.42.0.1')
if len(sys.argv) > 1:
	broker = sys.argv[1]
else:
	broker = '10.0.0.8'

client.connect('broker')
client.loop_start()


for frame in camera.capture_continuous(raw_capture, format='bgr', use_video_port=True):
	image = raw_capture.array
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#buff = cv2.imencode('.jpeg', gray)
	buff = bytearray(gray)
	client.publish('topic/video_frames', buff)
	raw_capture.truncate(0)
	time.sleep(0.1)

