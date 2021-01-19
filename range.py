#!/usr/bin/python3

from time import sleep
import mbultrasound

serialPort = "/dev/ttyAMA0"
# max depends on sensor
maxRange = 5000
sleepTime = 5
min_dist = 9999
max_dist = 0

while True :
	distance = mbultrasound.measure ( serialPort )
	if distance >= maxRange :
		print ( "Out of range" )
		sleep ( sleepTime )
		continue
	if distance < min_dist :
		min_dist = distance
	if distance > max_dist :
		max_dist = distance

	print ( distance,"mm" )
	sleep ( sleepTime )

#
