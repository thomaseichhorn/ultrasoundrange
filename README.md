# ultrasoundrange
Python script for ultrasound rangefinding with MB 100X EZ sensors


## Hardware connections

Sensor pin 1 <-> GND 
Sensor pin 2 <-> +5V 
Sensor pin 3 <-> Pi pin 10 (BCM 15 RXD) 


## Usage
Install python packages with
```
sudo pip install pyserial serial
```
Enable serial data on `ttyAM0` in `/boot/config.txt`:
```
enable_uart=1
dtoverlay=pi3-disable-bt
dtoverlay=pi3-miniuart-bt
```
Then run
```
sudo python range.py
```
