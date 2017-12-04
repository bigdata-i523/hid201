import grovepi
import time

grovepi.pinMode(3, "OUTPUT")
for i in [0, 1, 250, 0, 1, 250, 0]:
	print "writing: ", i
	grovepi.analogWrite(3, i)
	time.sleep(0.5)

