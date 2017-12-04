# Project

## IoT Application Using MQTT and Raspberry Pi Robot Car

### Abstract
As the number of connected edge devices increases there is a need for fast 
comunication between these devices, and to analyse the data collected by
these devices, which is made possible by the use of a scalable lightweight 
communicatoin protocol such as MQTT, which is easy to use, data agnostic, and 
application independent.
We look at one such appllication of the protocol, to control a robot car remotely,
over wireless network, navigating with the help of a raspberry pi camera on the car.


### Setup Instructions

* navigate into the project code directory

	*cd hid201/project/code/*

* First, the motors should be connected to the raspberry pi correctly.
the program uses the raspberr pi GPIO pins , and assumes that for the left motor, the pins IN1, IN2, IN3, IN4 are conected to GPIO pins 7, 11, 13, and 15, and for the right motor, they are connected to GPIO pins, 8, 10, 12, 16, as shown in the connection diagram in figure

* On the raspberry pi, dependencies for openCV need to be installed. Since the openCV is not available in pip for the arm processor in raspberry pi, we it must be installed from source. This takes a few hours on the raspberry pi. To complete the setup including installation of a MQTT client and opencv on the raspberry pi, clone the repository from github on the raspberry pi and navigate to the code folder, open the terminal and run the command

	*make setup_pi*

* Next, install opencv and an MQTT client and MQTT broker on the desktop. For this, clone the repository from github, navigate into the code folder and run the command 

	*make setup_server*

* Note the IP address of the desktop so that we an connect to the MQTT server running on it. Connect the raspberry pi and the desktop on the same wireless network. Run the command:

	*ifconfig*

* To run the code on the desktop, run the command:

	*make run_server IP=[ip address of the mqtt broker]*
this program can be exited by pressing 0

* Finally to run the code on the raspberry pi, run 

	* make run_pi IP=[ip address of the mqtt broker]*
this program can be exited by pressing ctrl + c on the keyboard

* To end the programs running in background, or to end all programs run the following command on the raspberry pi and the desktop

	*make kill*


### Code
The code for the project is available <a href="https://github.com/bigdata-i523/hid201/tree/master/project/code">here</a>

### Additional Notes
* Installing opencv on the raspberry pi is included in the Makefile, however it takes a long time
Thus for convenience it may be easier to use an SD card that has opencv installed

* The complete working setup of the raspberry pi can be found at smith research center.
* The program wasn not added to rc.local as we dont know bwforehand the IP address of the MQTT broker
* You can also use Makefile to setup the libraries if testing on a new raspberry pi.
