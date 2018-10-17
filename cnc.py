#!/usr/bin/env python
      
import time
import serial
import json

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0

data = {
		"cmd": "setToolCount",
		"deviceid":"107",
		"timestamp":123,
        "cnc": "107",
        "vc87":24,
        "vc92":21
	}

#with open("data_file.json", "w") as write_file:
 #   json.dump(data, write_file)

json_string = json.dumps(data)    
ser.write(json_string.encode())
#while 1:
#    ser.write(b'{"vc87":%d}'%(counter))
#    time.sleep(5)
#    counter += 1
