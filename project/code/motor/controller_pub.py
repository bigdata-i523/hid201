from __future__ import print_function
import paho.mqtt.client as mqtt
import time
import sys
import tty, termios

def getch():
	## obtained from http://code.activestate.com/recipes/577977-get-single-keypress/
        """getch() -> key character

        Read a single keypress from stdin and return the resulting character. 
        Nothing is echoed to the console. This call will block if a keypress 
        is not already available, but will not wait for Enter to be pressed. 

        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



def on_connect(client, user_data, flags, rc):
	if rc == 0:
		print("connected successfully")
	else:
		print( "error while connecting")

def on_log(client, user_data, level, buff):
	print( "log :"+ str( buff))

client = mqtt.Client("controller")
client.on_connect = on_connect
client.on_log = on_log

if len(sys.argv) > 1:
	broker = sys.argv[1]
else:
	broker = '127.0.0.1'

client.connect(broker)
client.loop_start()

while True:
	ch = getch()
	print("Press 0 to exit")
	if ch == "0":
		print( "exiting")
		exit()
	elif ch == "w":
		client.publish('topic/control', "F")
	elif ch == "a":
		client.publish('topic/control', "L")
	elif ch == "s":
		client.publish('topic/control', "B")
	elif ch == "d":
		client.publish('topic/control', "R")
	time.sleep(0.1)
clientloop_stop()
