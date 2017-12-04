test:
	echo $(IP)
	python mqtt_video/vid_sub.py $(IP)
setup_server:
	sudo apt-get install mosquitto
	sudo apt-get install libmosquitto-dev
	pip install opencv-python
	pip install paho-mqtt

setup_pi:
	#install dependencies for opencv
	curl >> opencv.zip
	unzip
	cd openv
	mkdir build
	cd build
	cmake
	make install

run_server:
	# run videosubscriber and motoro controller on desktop
	python mqtt_video/vid_sub.py $(IP) & jobs -p > .pid1
	python motor/controller_pub.py $(IP) ; jobs -p > .pid2

run_pi:
	# run video publisher and motor controller on pi
	python mqtt_video/vid_pub.py $(IP) & jobs -p > .pid1
	python motor/controller_stepper_sub.py $(IP) & jobs -p > .pid2

kill:
	kill -9 `cat .pid1`

