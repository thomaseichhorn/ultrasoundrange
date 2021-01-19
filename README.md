# ultrasoundrange
Python script for ultrasound rangefinding with MB sensors

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
