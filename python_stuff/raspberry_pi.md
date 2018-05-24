## Using Raspberry pi

### Setup instructions
The easiest way to set up raspbian on the pi is using NOOBS , which can be found on the github page <a href = "https://github.com/raspberrypi/noobs">here</a>

### Change Default password
Once the raspberry pi is set up, log in to the raspberry pi,
using a monitor, or via ssh.
* type in comand sudo raspi-config
* the raspberry pi configuration dialog box will appear
* navigate to Change Default Password option and press Enter
* type in the old password to raspberry pi (default password: raspberry) 
* type in the new password you want to set
* type the password to confirm
* once youare back at the configuration dialog box, select <Finish>

Now the default password to your raspbery pi has been changed

### Python on raspbery pi
In recent versions of raspbian python is preinstalled with the basic gpio 
support and we dont need additional libraries to start working with gpio pins

To check if python is installed
* open terminal and type : which python
this will give you the path where python is installed
* to install gpio support type command sudo apt-get install python-rpi.gpio
* use python3-rpi.gpio for python 3

more details can be found at <https://www.raspberrypi.org/documentation/usage/python/more.md>

### Some elementary python
* open terminal on raspbery pi and type python to open python2 shell
* now you can use python shell to run commands like

```
>>> x = 1 + 2
>>> y = x + 2
>>> print y
5
>>> 
```

### Getting on wifi
To connect to the internet using raspberry pis wifi, 
set wifi
connect to laptop via lan
change default gateway of the network profile to pi's ip address
change pis default gateway to pis ip address
connect to wifi via pi

* connect raspberry pi to a monitor viaHDMI cable and attach power cable to boot the pi
* connect a keyboard and mouse with help of the usb port
* go to the network settings
* select the wifi access point that you need to connect to 
* enter the password when asked
* you wil now be connected to the network 

We sould try to use IU secure as it is an authenticated access to the internet
attwifi is an open connection and anyone can connect to it, some sites which require https will warn you and may not open
also connecting to open wifi networks increases the risk of attacks like evil twin acess point
