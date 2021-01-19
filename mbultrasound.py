#!/usr/bin/python3

from time import time
from serial import Serial

serialDevice = "/dev/ttyAMA0"
# seconds to try for a good reading before quitting
maxwait = 3

def measure ( portName ) :
	ser = Serial ( portName, 9600, 8, 'N', 1, timeout = 1 )
	timeStart = time ( )
	valueCount = 0

	while time ( ) < timeStart + maxwait :
		if ser.inWaiting ( ) :
			bytesToRead = ser.inWaiting ( )
			valueCount += 1

			# 1st reading may be partial number; throw it out
			if valueCount < 2 :
				continue

			testData = ser.read ( bytesToRead )

			# data received did not start with R
			if not testData.startswith ( b'R' ) :
				continue

			try :
				sensorData = testData.decode ( 'utf-8' ) .lstrip ( 'R' )
			# data received could not be decoded properly
			except UnicodeDecodeError :
				continue

			try :
				mm = int ( sensorData )
			# value is not a number
			except ValueError :
				continue

			ser.close ( )
			return ( mm )

	ser.close ( )
	raise RuntimeError ( "Expected serial data not received" )

if __name__ == '__main__' :
	measurement = measure ( serialDevice )
	print ( "distance =", measurement )

#
