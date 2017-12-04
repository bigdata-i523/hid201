setup_server:
	# install mqtt broker and client libraies on desktop
	sudo apt-get install mosquitto
	sudo apt-get install libmosquitto-dev
	pip install opencv-python
	pip install paho-mqtt

setup_pi:
	#install dependencies for opencv and mqtt on raspberry pi
	echo 'Installing mqtt'
	pip install paho-mqtt

	echo 'installing dependencies for opencv'
	sudo apt-get update && sudo apt-get upgrade
	sudo apt-get install build-essential cmake pkg-config
	sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
	sudo apt-get install libxvidcore-dev libx264-dev
	sudo apt-get install libgtk2.0-dev libgtk-3-dev
	sudo apt-get install libatlas-base-dev gfortran
	sudo apt-get install python2.7-dev python3-dev

	echo 'downloading opencv'
	cd ~
	wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
	unzip opencv.zip
	wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
	unzip opencv_contrib.zip
	wget https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py

	echo 'installing numpy...might take a while'
	pip install numpy

	echo 'instaling opencv...this is going to take a while'
	echo 'around 4 hours on raspberry pi 3'
	cd ~/opencv-3.3.0/
	mkdir build
	cd build
	mkdir build
	cd build
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
    	-D CMAKE_INSTALL_PREFIX=/usr/local \
    	-D INSTALL_PYTHON_EXAMPLES=ON \
    	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
    	-D BUILD_EXAMPLES=ON ..
	make
	sudo make install
	sudo ldconfig
	cd ~/.local/lib/python2.7/site-packages
	ln -s  /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

run_server:
	# run videosubscriber and motoro controller on desktop
	python mqtt_video/vid_sub.py $(IP) & jobs -p > .pid1
	python motor/controller_pub.py $(IP) ; jobs -p > .pid2

run_pi:
	# run video publisher and motor controller on pi
	python mqtt_video/vid_pub.py $(IP) & jobs -p > .pid1
	python motor/controller_stepper_sub.py $(IP) & jobs -p > .pid2

kill:
	# kill the processes
	kill -9 `cat .pid1`
	kill -9 `cat .pid2`
	rm .pid1 .pid2
