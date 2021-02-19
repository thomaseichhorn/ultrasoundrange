# ultrasoundrange
Python scripts for ultrasound rangefinding with MB 100X EZ sensors on a Raspberry Pi


## Hardware connections
Depending on your sensor, you might have to solder the connection on the back side of the sensor to enable serial data output.
```
Sensor pin 1 <-> GND
Sensor pin 2 <-> +5V
Sensor pin 3 <-> Pi pin 10 (BCM 15 RXD)
```


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

### Raspberry Pi 4
If you are running a Pi4, change "/dev/ttyAMA0" to "/dev/ttyAMA1" in `mbultrasound.py` and `range.py` and add the additional line `dtoverlay=uart2` to `/boot/config.txt`.
Connect sensor pin 3 to Pi pin 28 (BCM 1).
